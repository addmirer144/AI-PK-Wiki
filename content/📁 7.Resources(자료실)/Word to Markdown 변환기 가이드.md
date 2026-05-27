---
id: 20250924002
type: guide
created: 2025-09-24
updated: 2025-09-24
tags: #도구 #자동화 #word변환 #마크다운 #옵시디언 #가이드
---

# Word to Markdown 변환기 가이드

## 🎯 개요

이 도구는 Obsidian 볼트 내의 Word 파일(.docx, .doc)을 자동으로 마크다운(.md) 형식으로 변환해주는 서브어시스턴트입니다.

### 주요 기능
- ✅ Word 파일을 마크다운으로 일괄 변환
- ✅ 자동 감시 모드 (새 파일 자동 변환)
- ✅ Obsidian 메타데이터 자동 생성
- ✅ 이미지 및 첨부파일 추출
- ✅ 태그 자동 분류
- ✅ 변환 로그 생성

## 🚀 빠른 시작

### 1단계: 초기 설정
```bash
# 터미널에서 볼트 디렉토리로 이동
cd "/Users/addmirer/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI-PK M-System"

# 의존성 설치
./convert.sh --setup
```

### 2단계: 사용법
```bash
# 모든 Word 파일 변환
./convert.sh

# 특정 파일만 변환
./convert.sh --file "설교문.docx"

# 자동 감시 모드 (새 Word 파일 자동 변환)
./convert.sh --watch
```

## 📋 상세 사용법

### 일괄 변환 모드
```bash
./convert.sh
```
- 볼트 내의 모든 Word 파일을 검색하여 마크다운으로 변환
- 변환된 파일은 `📁 2.Processed_Notes(가공된노트)` 폴더에 저장
- 변환 로그 `word_conversion_log.md` 자동 생성

### 특정 파일 변환
```bash
./convert.sh --file "경로/파일명.docx"
```
- 지정된 파일만 변환
- 상대 경로 또는 절대 경로 사용 가능

### 자동 감시 모드
```bash
./convert.sh --watch
```
- 볼트를 실시간 감시
- 새로운 Word 파일이 추가되면 자동으로 변환
- macOS 알림으로 변환 완료 통보
- `Ctrl+C`로 중지

### 직접 Python 스크립트 실행
```bash
# 기본 변환
python3 word_to_markdown.py

# 옵션들
python3 word_to_markdown.py --help
python3 word_to_markdown.py --dry-run  # 실제 변환 없이 파일 목록만 표시
python3 word_to_markdown.py --output /custom/path  # 커스텀 출력 경로
```

## 🔧 변환 결과물

### 생성되는 파일 구조
```
📁 2.Processed_Notes(가공된노트)/
├── 변환된_파일.md
├── attachments/
│   ├── image1.png
│   └── image2.jpg
└── word_conversion_log.md
```

### 메타데이터 (Frontmatter) 예시
```yaml
---
id: 20250924123456
type: processed
created: 2025-03-30 21:03
updated: 2025-09-24 12:30
converted: 2025-09-24 15:45:20
original_file: 설교문.docx
tags: #새벽묵상 #복음서 #설교 #변환됨
---

# 파일명

> **원본**: `설교문.docx`  
> **변환일시**: 2025-09-24 15:45:20

[변환된 내용...]
```

### 자동 태그 분류
- `#새벽묵상`: 파일명에 '새벽' 포함
- `#청소년설교`: 파일명에 '청소년' 포함  
- `#아침묵상`: 파일명에 '아침묵상' 포함
- `#복음서`: 마태복음, 마가복음, 누가복음, 요한복음 언급
- `#구약`: 구약 성경 책 이름 포함
- `#설교`, `#변환됨`: 기본 태그

## ⚙️ 설정 및 커스터마이징

### 출력 디렉토리 변경
```python
# word_to_markdown.py 파일에서 수정
output_dir = word_file.parent / "📁 사용자정의폴더"
```

### 태그 규칙 수정
```python
# word_to_markdown.py의 add_frontmatter 함수에서 태그 로직 수정
if '새로운키워드' in filename_lower:
    tags.append('#새로운태그')
```

### 제외할 폴더 설정
```python
# 특정 폴더 제외하고 싶은 경우
EXCLUDE_DIRS = ['Archive', 'Backup', '.obsidian']
```

## 🚨 문제 해결

### 일반적인 문제들

#### 1. "Pandoc이 설치되어 있지 않습니다"
```bash
# macOS
brew install pandoc

# 또는 공식 설치 프로그램 다운로드
# https://pandoc.org/installing.html
```

#### 2. "watchdog 모듈이 설치되어 있지 않습니다"
```bash
pip3 install watchdog --user
```

#### 3. "Permission denied" 오류
```bash
chmod +x convert.sh
chmod +x word_to_markdown.py
chmod +x watch_and_convert.py
```

#### 4. 변환 실패하는 경우
- Word 파일이 손상되었는지 확인
- 파일이 다른 프로그램에서 열려있는지 확인
- 파일 경로에 특수문자가 있는지 확인

#### 5. 이미지가 변환되지 않는 경우
- Word 파일에 이미지가 제대로 삽입되었는지 확인
- `attachments` 폴더에 이미지 파일이 생성되었는지 확인

## 🎛️ 고급 사용법

### 배치 스크립트로 스케줄링
```bash
# cron 작업으로 매일 자동 변환
# crontab -e 에서 추가:
0 9 * * * cd "/path/to/vault" && ./convert.sh
```

### 변환 로그 활용
변환 완료 후 생성되는 `word_conversion_log.md` 파일을 통해:
- 변환된 파일들을 Obsidian에서 쉽게 탐색
- 변환 히스토리 추적
- 다음 작업 단계 확인

### 커스텀 후처리
변환 후 추가 작업이 필요한 경우:
```python
def custom_post_process(markdown_file):
    """변환 후 커스텀 처리"""
    # 특정 텍스트 패턴 수정
    # 추가 메타데이터 삽입
    # 다른 노트와 자동 링크 생성
    pass
```

## 📈 활용 사례

### 설교 준비 워크플로우
1. Word로 설교문 작성
2. 볼트에 저장하면 자동 변환
3. Obsidian에서 다른 노트들과 연결
4. 태그를 통한 주제별 분류

### 연구 자료 관리
1. Word 형태의 연구 노트들을 일괄 변환
2. 마크다운 형식으로 통일된 지식베이스 구축
3. 검색과 연결이 용이한 형태로 관리

### 협업 문서 통합
1. 다른 사람이 작성한 Word 문서들을 수집
2. 마크다운으로 변환하여 통일된 형식으로 관리
3. Obsidian의 연결 기능을 활용한 지식 네트워크 구축

## 🔗 연결 노트

### 관련 방법론
- [[세컨드 브레인의 네가지 장점]] ← 이 도구가 구현하는 핵심 원리
- [[제텔카스텐 - 니클라스 루만의 지식 생산 시스템]]
- [[옵시디언을 활용한 제텔카스텐 구축법]]
- [[개인 지식 관리 시스템 설계]]

### 자동화와 워크플로우
- [[학습 시스템의 자동화]]
- [[글쓰기 워크플로우와 아이디어 발전]]
- [[AI 도구와 세컨드 브레인의 협업]]

### 실제 활용 사례
- [[설교 준비와 지식 관리]]
- [[연구 노트의 디지털 변환]]
- [[협업 문서의 통합 관리]]

## 📝 업데이트 로그

### v1.0 (2025-09-24)
- ✅ 기본 변환 기능 구현
- ✅ 자동 감시 모드 추가
- ✅ 메타데이터 자동 생성
- ✅ 태그 자동 분류
- ✅ 이미지 추출 기능
- ✅ 사용자 가이드 작성

### 계획된 기능
- [ ] GUI 인터페이스 추가
- [ ] 클라우드 동기화 감지
- [ ] 변환 규칙 커스터마이징 UI
- [ ] 다른 파일 형식 지원 (PDF, EPUB 등)

---

> 💡 **팁**: 이 도구는 [[세컨드 브레인의 네가지 장점]]에서 설명하는 "아이디어 구체화"와 "시간을 둔 발전"을 실현하는 구체적인 도구입니다. Word 파일로 작성된 초기 아이디어들을 마크다운으로 변환함으로써 Obsidian의 연결 기능을 활용한 지식 네트워크 구축이 가능해집니다.