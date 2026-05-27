#!/usr/bin/env python3
"""
Word to Markdown Converter for Obsidian
볼트 내의 Word 파일을 마크다운으로 자동 변환하는 도구
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import subprocess
import shutil

def check_pandoc():
    """pandoc 설치 여부 확인"""
    if shutil.which("pandoc") is None:
        print("❌ Pandoc이 설치되어 있지 않습니다.")
        print("설치 방법:")
        print("  macOS: brew install pandoc")
        print("  또는 https://pandoc.org/installing.html 참고")
        sys.exit(1)
    else:
        print("✅ Pandoc 발견됨")

def find_word_files(vault_path):
    """볼트에서 Word 파일 찾기"""
    word_files = []
    vault_path = Path(vault_path)
    
    # .docx와 .doc 파일 검색
    for ext in ['*.docx', '*.doc']:
        word_files.extend(vault_path.rglob(ext))
    
    return sorted(word_files)

def sanitize_filename(filename):
    """파일명을 Obsidian에 적합하게 정리"""
    # 특수문자 제거하고 공백을 하이픈으로 변경
    import re
    name = re.sub(r'[<>:"/\\|?*]', '', filename)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def convert_word_to_markdown(word_file, output_dir=None):
    """Word 파일을 마크다운으로 변환"""
    word_file = Path(word_file)
    
    # 출력 디렉토리 설정
    if output_dir is None:
        output_dir = word_file.parent / "📁 2.Processed_Notes(가공된노트)"
    else:
        output_dir = Path(output_dir)
    
    # 출력 디렉토리 생성
    output_dir.mkdir(exist_ok=True)
    
    # 출력 파일명 생성
    base_name = sanitize_filename(word_file.stem)
    output_file = output_dir / f"{base_name}.md"
    
    print(f"🔄 변환 중: {word_file.name}")
    
    try:
        # pandoc을 사용한 변환
        cmd = [
            "pandoc",
            str(word_file),
            "-t", "markdown",
            "-o", str(output_file),
            "--extract-media", str(output_dir / "attachments"),  # 이미지 추출
            "--wrap=none",  # 줄 바꿈 방지
            "--markdown-headings=atx",  # # 스타일 헤딩 사용
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 변환된 파일에 메타데이터 추가
        add_frontmatter(output_file, word_file)
        
        print(f"✅ 변환 완료: {output_file.name}")
        return output_file
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 변환 실패: {word_file.name}")
        print(f"   오류: {e.stderr}")
        return None
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        return None

def add_frontmatter(markdown_file, original_word_file):
    """마크다운 파일에 Obsidian 메타데이터 추가"""
    markdown_file = Path(markdown_file)
    original_word_file = Path(original_word_file)
    
    # 기존 내용 읽기
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 파일 정보 수집
    created_time = datetime.fromtimestamp(original_word_file.stat().st_birthtime)
    modified_time = datetime.fromtimestamp(original_word_file.stat().st_mtime)
    
    # 태그 추출 (파일명에서)
    filename_lower = original_word_file.name.lower()
    tags = []
    if '새벽' in filename_lower:
        tags.append('#새벽묵상')
    if '청소년' in filename_lower:
        tags.append('#청소년설교')
    if '아침묵상' in filename_lower:
        tags.append('#아침묵상')
    if any(book in filename_lower for book in ['마태복음', '마가복음', '누가복음', '요한복음']):
        tags.append('#복음서')
    if '신명기' in filename_lower or '룻기' in filename_lower:
        tags.append('#구약')
    
    # 기본 태그 추가
    tags.extend(['#설교', '#변환됨'])
    
    # Frontmatter 생성
    frontmatter = f"""---
id: {datetime.now().strftime('%Y%m%d%H%M%S')}
type: processed
created: {created_time.strftime('%Y-%m-%d %H:%M')}
updated: {modified_time.strftime('%Y-%m-%d %H:%M')}
converted: {datetime.now().strftime('%Y-%m-%d %H:%M')}
original_file: {original_word_file.name}
tags: {' '.join(tags)}
---

# {markdown_file.stem}

> **원본**: `{original_word_file.name}`  
> **변환일시**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""
    
    # 새로운 내용으로 덮어쓰기
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

def create_conversion_log(converted_files, vault_path):
    """변환 로그 생성"""
    log_file = Path(vault_path) / "word_conversion_log.md"
    
    log_content = f"""# Word to Markdown 변환 로그

**변환 일시**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**변환된 파일 수**: {len(converted_files)}

## 변환된 파일 목록

"""
    
    for i, file_path in enumerate(converted_files, 1):
        log_content += f"{i}. [[{Path(file_path).stem}]]\n"
    
    log_content += f"""

## 다음 단계

- [ ] 변환된 파일들 검토하기
- [ ] 필요한 경우 수동으로 포맷팅 조정
- [ ] 원본 Word 파일 아카이브 또는 삭제 결정
- [ ] 연결 노트 생성하기

---
*자동 생성된 로그 파일*
"""
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"📝 변환 로그 생성: {log_file}")

def main():
    parser = argparse.ArgumentParser(description="Word 파일을 마크다운으로 변환")
    parser.add_argument("vault_path", nargs='?', 
                       default="/Users/addmirer/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI-PK M-System",
                       help="Obsidian 볼트 경로")
    parser.add_argument("--file", "-f", help="특정 파일만 변환")
    parser.add_argument("--output", "-o", help="출력 디렉토리 지정")
    parser.add_argument("--dry-run", action="store_true", help="실제 변환 없이 파일 목록만 표시")
    
    args = parser.parse_args()
    
    print("🚀 Word to Markdown 변환기 시작")
    print("="*50)
    
    # pandoc 확인
    check_pandoc()
    
    # 볼트 경로 확인
    vault_path = Path(args.vault_path)
    if not vault_path.exists():
        print(f"❌ 볼트 경로를 찾을 수 없습니다: {vault_path}")
        sys.exit(1)
    
    print(f"📁 볼트 경로: {vault_path}")
    
    # Word 파일 찾기
    if args.file:
        word_files = [Path(args.file)]
        if not word_files[0].exists():
            print(f"❌ 파일을 찾을 수 없습니다: {args.file}")
            sys.exit(1)
    else:
        word_files = find_word_files(vault_path)
    
    if not word_files:
        print("📄 변환할 Word 파일이 없습니다.")
        return
    
    print(f"📊 발견된 Word 파일: {len(word_files)}개")
    
    # 파일 목록 표시
    for i, file in enumerate(word_files, 1):
        relative_path = file.relative_to(vault_path)
        print(f"  {i:2d}. {relative_path}")
    
    if args.dry_run:
        print("\n🔍 Dry run 모드: 실제 변환을 수행하지 않습니다.")
        return
    
    # 사용자 확인
    if len(word_files) > 1:
        response = input(f"\n{len(word_files)}개 파일을 모두 변환하시겠습니까? (y/N): ")
        if response.lower() != 'y':
            print("변환을 취소합니다.")
            return
    
    print("\n🔄 변환 시작...")
    print("-" * 50)
    
    # 변환 실행
    converted_files = []
    failed_files = []
    
    for word_file in word_files:
        result = convert_word_to_markdown(word_file, args.output)
        if result:
            converted_files.append(result)
        else:
            failed_files.append(word_file)
    
    # 결과 요약
    print("\n" + "="*50)
    print("🎉 변환 완료!")
    print(f"✅ 성공: {len(converted_files)}개")
    print(f"❌ 실패: {len(failed_files)}개")
    
    if failed_files:
        print("\n실패한 파일들:")
        for file in failed_files:
            print(f"  - {file.name}")
    
    # 변환 로그 생성
    if converted_files:
        create_conversion_log(converted_files, vault_path)
    
    print(f"\n📁 변환된 파일들은 다음 위치에 저장되었습니다:")
    if args.output:
        print(f"  {args.output}")
    else:
        print(f"  각 원본 파일 디렉토리의 '📁 2.Processed_Notes(가공된노트)' 폴더")

if __name__ == "__main__":
    main()