#!/usr/bin/env python3
"""
Word 파일 자동 감지 및 변환 서비스
새로운 Word 파일이 볼트에 추가되면 자동으로 마크다운으로 변환
"""

import os
import time
import threading
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys

class WordFileHandler(FileSystemEventHandler):
    def __init__(self, vault_path, converter_script):
        self.vault_path = Path(vault_path)
        self.converter_script = Path(converter_script)
        self.processing_files = set()  # 중복 처리 방지
        
    def on_created(self, event):
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        
        # Word 파일인지 확인
        if file_path.suffix.lower() in ['.docx', '.doc']:
            self.process_word_file(file_path)
    
    def on_moved(self, event):
        if event.is_directory:
            return
            
        dest_path = Path(event.dest_path)
        
        # Word 파일이 이동되어 왔는지 확인
        if dest_path.suffix.lower() in ['.docx', '.doc']:
            self.process_word_file(dest_path)
    
    def process_word_file(self, file_path):
        """Word 파일을 처리하고 변환"""
        if file_path in self.processing_files:
            return  # 이미 처리 중
            
        self.processing_files.add(file_path)
        
        try:
            print(f"🔍 새로운 Word 파일 감지: {file_path.name}")
            
            # 파일이 완전히 복사될 때까지 잠시 대기
            time.sleep(2)
            
            # 파일이 아직 존재하는지 확인
            if not file_path.exists():
                print(f"⚠️ 파일이 더 이상 존재하지 않습니다: {file_path.name}")
                return
            
            # 변환 스크립트 실행
            cmd = [
                sys.executable,
                str(self.converter_script),
                str(self.vault_path),
                "--file", str(file_path)
            ]
            
            print(f"🔄 자동 변환 시작: {file_path.name}")
            
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                timeout=300  # 5분 타임아웃
            )
            
            if result.returncode == 0:
                print(f"✅ 자동 변환 완료: {file_path.name}")
                
                # 성공 알림 (선택사항)
                self.send_notification(f"Word 파일 변환 완료: {file_path.name}")
            else:
                print(f"❌ 변환 실패: {file_path.name}")
                print(f"   오류: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print(f"⏰ 변환 시간 초과: {file_path.name}")
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {e}")
        finally:
            self.processing_files.discard(file_path)
    
    def send_notification(self, message):
        """macOS 알림 전송"""
        try:
            subprocess.run([
                "osascript", "-e", 
                f'display notification "{message}" with title "Obsidian Word Converter"'
            ], check=False)
        except:
            pass  # 알림 실패해도 무시

class WordWatcher:
    def __init__(self, vault_path, converter_script):
        self.vault_path = Path(vault_path)
        self.converter_script = Path(converter_script)
        self.observer = None
        self.running = False
        
    def start(self):
        """감시 시작"""
        if self.running:
            print("⚠️ 이미 감시가 실행 중입니다.")
            return
            
        print(f"🚀 Word 파일 자동 변환 감시 시작")
        print(f"📁 감시 경로: {self.vault_path}")
        print(f"🔧 변환기: {self.converter_script}")
        print("=" * 50)
        
        event_handler = WordFileHandler(self.vault_path, self.converter_script)
        self.observer = Observer()
        self.observer.schedule(event_handler, str(self.vault_path), recursive=True)
        
        self.observer.start()
        self.running = True
        
        print("👁️ Word 파일 감시가 시작되었습니다.")
        print("   새로운 Word 파일(.docx, .doc)이 감지되면 자동으로 변환됩니다.")
        print("   중지하려면 Ctrl+C를 누르세요.")
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """감시 중지"""
        if self.observer and self.running:
            print("\n🛑 감시를 중지합니다...")
            self.observer.stop()
            self.observer.join()
            self.running = False
            print("✅ 감시가 중지되었습니다.")

def check_dependencies():
    """필요한 의존성 확인"""
    print("🔍 의존성 확인 중...")
    
    # pandoc 확인
    if not subprocess.run(["which", "pandoc"], capture_output=True).returncode == 0:
        print("❌ Pandoc이 설치되어 있지 않습니다.")
        print("설치: brew install pandoc")
        return False
    
    # watchdog 모듈 확인
    try:
        import watchdog
        print("✅ 모든 의존성이 확인되었습니다.")
        return True
    except ImportError:
        print("❌ watchdog 모듈이 설치되어 있지 않습니다.")
        print("설치: pip install watchdog")
        return False

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Word 파일 자동 감지 및 변환 서비스")
    parser.add_argument("vault_path", nargs='?',
                       default="/Users/addmirer/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI-PK M-System",
                       help="Obsidian 볼트 경로")
    parser.add_argument("--converter", "-c",
                       help="변환 스크립트 경로 (기본: 같은 디렉토리의 word_to_markdown.py)")
    parser.add_argument("--daemon", "-d", action="store_true",
                       help="백그라운드에서 실행")
    
    args = parser.parse_args()
    
    # 의존성 확인
    if not check_dependencies():
        sys.exit(1)
    
    # 경로 설정
    vault_path = Path(args.vault_path)
    if not vault_path.exists():
        print(f"❌ 볼트 경로를 찾을 수 없습니다: {vault_path}")
        sys.exit(1)
    
    if args.converter:
        converter_script = Path(args.converter)
    else:
        converter_script = Path(__file__).parent / "word_to_markdown.py"
    
    if not converter_script.exists():
        print(f"❌ 변환 스크립트를 찾을 수 없습니다: {converter_script}")
        sys.exit(1)
    
    # 감시자 생성 및 시작
    watcher = WordWatcher(vault_path, converter_script)
    
    if args.daemon:
        # 백그라운드 실행을 위한 데몬화 (간단한 버전)
        print("🔧 백그라운드 모드는 아직 구현되지 않았습니다.")
        print("   현재는 터미널에서 직접 실행해주세요.")
        sys.exit(1)
    
    watcher.start()

if __name__ == "__main__":
    main()