#!/bin/bash
#
# Word to Markdown 변환기 실행 스크립트
# 사용법:
#   ./convert.sh              # 모든 Word 파일 변환
#   ./convert.sh --watch      # 자동 감시 모드  
#   ./convert.sh --help       # 도움말
#

# 스크립트 경로 설정
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_PATH="$SCRIPT_DIR"
CONVERTER="$SCRIPT_DIR/word_to_markdown.py"
CONVERTER_PYTHON="$SCRIPT_DIR/word_to_markdown_python.py"
WATCHER="$SCRIPT_DIR/watch_and_convert.py"

# 함수: 도움말 출력
show_help() {
    echo "🔧 Obsidian Word to Markdown 변환기"
    echo "=================================="
    echo ""
    echo "📋 기능:"
    echo "  ✅ Word(.docx/.doc) → Markdown 자동 변환"
    echo "  ✅ Obsidian 메타데이터 자동 생성"
    echo "  ✅ 태그 자동 분류 (#새벽묵상 #청소년설교 등)"
    echo "  ✅ 이미지 및 첨부파일 추출"
    echo "  ✅ 실시간 파일 감시 모드"
    echo ""
    echo "🚀 사용법:"
    echo "  $0                    모든 Word 파일을 마크다운으로 변환"
    echo "  $0 --watch           자동 감시 모드 (새 Word 파일 자동 변환)"
    echo "  $0 --file <파일>     특정 파일만 변환"
    echo "  $0 --setup           초기 설정 (의존성 설치)"
    echo "  $0 --help            이 도움말 표시"
    echo ""
    echo "💡 예제:"
    echo "  $0 --file \"설교문.docx\""
    echo "  $0 --watch"
    echo ""
    echo "🔧 변환 엔진:"
    echo "  • Pandoc 설치 시: 고품질 변환 (권장)"
    echo "  • Pandoc 미설치 시: Python 기반 변환"
}

# 함수: 의존성 설치
setup_dependencies() {
    echo "🔧 의존성 설치 중..."
    
    # Homebrew 확인
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew가 설치되어 있지 않습니다."
        echo "   https://brew.sh 에서 설치해주세요."
        exit 1
    fi
    
    # Pandoc 설치
    if ! command -v pandoc &> /dev/null; then
        echo "📦 Pandoc 설치 중..."
        brew install pandoc
    else
        echo "✅ Pandoc 이미 설치됨"
    fi
    
    # Python 패키지 설치
    echo "🐍 Python 패키지 설치 중..."
    pip3 install watchdog python-docx mammoth --user
    
    echo "✅ 설정 완료!"
    echo ""
    echo "이제 다음 명령을 실행할 수 있습니다:"
    echo "  $0           # 모든 Word 파일 변환"
    echo "  $0 --watch   # 자동 감시 시작"
}

# 메인 실행 부분
main() {
    case "${1:-}" in
        --help|-h)
            show_help
            ;;
        --setup)
            setup_dependencies
            ;;
        --watch|-w)
            echo "🚀 자동 감시 모드 시작..."
            python3 "$WATCHER" "$VAULT_PATH"
            ;;
        --file|-f)
            if [[ -z "${2:-}" ]]; then
                echo "❌ 파일 경로를 지정해주세요."
                echo "예: $0 --file \"파일명.docx\""
                exit 1
            fi
            echo "🔄 파일 변환: $2"
            # Pandoc이 있으면 원본 변환기 사용, 없으면 Python 버전 사용
            if command -v pandoc &> /dev/null; then
                echo "📦 Pandoc 감지: 고품질 변환기 사용"
                python3 "$CONVERTER" "$VAULT_PATH" --file "$2"
            else
                echo "🐍 Python 변환기 사용 (Pandoc 미설치)"
                python3 "$CONVERTER_PYTHON" "$VAULT_PATH" --file "$2"
            fi
            ;;
        "")
            echo "🔄 모든 Word 파일 변환 시작..."
            # Pandoc이 있으면 원본 변환기 사용, 없으면 Python 버전 사용
            if command -v pandoc &> /dev/null; then
                echo "📦 Pandoc 감지: 고품질 변환기 사용"
                python3 "$CONVERTER" "$VAULT_PATH"
            else
                echo "🐍 Python 변환기 사용 (Pandoc 미설치)"
                python3 "$CONVERTER_PYTHON" "$VAULT_PATH"
            fi
            ;;
        *)
            echo "❌ 알 수 없는 옵션: $1"
            echo "도움말을 보려면: $0 --help"
            exit 1
            ;;
    esac
}

# 스크립트 실행
main "$@"