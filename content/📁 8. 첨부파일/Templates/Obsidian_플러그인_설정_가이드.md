---
id: obsidian_plugin_guide
type: tutorial
created: 2025-10-16
updated: 2025-10-16
tags: #Obsidian #플러그인 #자동화 #생산성 #가이드
---

# Obsidian 플러그인 설정 가이드

> 제텔카스텐 시스템을 위한 필수 플러그인
> **자동화를 통한 생산성 향상**
> 소요 시간: 약 1시간

---

## 🎯 개요

### 설치할 플러그인 (우선순위순)

| 플러그인 | 우선순위 | 용도 | 효과 |
|----------|---------|------|------|
| Dataview | ⭐⭐⭐ 필수 | 자동 목록 생성 | 인덱스 자동 업데이트 |
| Templater | ⭐⭐⭐ 필수 | 템플릿 자동화 | 신속한 파일 생성 |
| Calendar | ⭐⭐ 추천 | 날짜별 노트 관리 | 시각적 일정 관리 |
| Tag Wrangler | ⭐⭐ 추천 | 태그 관리 | 태그 정리 자동화 |
| Recent Files | ⭐ 편의 | 빠른 접근 | 작업 효율 향상 |

---

## 📦 1. Dataview 플러그인 ⭐⭐⭐

### 1.1 설치 방법

1. **Obsidian 열기** → 좌측 하단 ⚙️ (설정) 클릭
2. **커뮤니티 플러그인** → "안전 모드 끄기"
3. **탐색** 버튼 클릭
4. 검색창에 **"Dataview"** 입력
5. **설치** → **활성화**

### 1.2 기본 설정

**설정** → **Dataview** → 다음 옵션 활성화:
- ✅ **Enable JavaScript Queries**
- ✅ **Enable Inline Queries**
- ✅ **Enable Inline JavaScript Queries**

### 1.3 사용 예시

#### 예시 1: 새벽기도회 설교 목록 자동 생성

**인덱스 파일에 추가**:
````markdown
```dataview
TABLE WITHOUT ID
  file.link as "설교",
  regexreplace(file.name, "\[새벽\] (\d+) (.+)", "$2") as "제목",
  file.ctime as "작성일"
FROM "4.Prolific_Lounge/설교/새벽기도회"
SORT file.name DESC
LIMIT 10
```
````

**결과**:
| 설교 | 제목 | 작성일 |
|------|------|--------|
| [[새벽] 251017...]] | 보는 눈을 열어주소서... | 2025-10-17 |
| [[새벽] 250918...]] | 거룩함에 이르는... | 2025-09-18 |

---

#### 예시 2: 이번 달 작성한 설교

**월간 리뷰에 추가**:
````markdown
```dataview
TABLE file.link as "파일", file.ctime as "날짜"
FROM "4.Prolific_Lounge"
WHERE file.ctime >= date(2025-10-01) AND file.ctime < date(2025-11-01)
SORT file.ctime DESC
```
````

---

#### 예시 3: 특정 태그가 있는 노트

````markdown
```dataview
LIST
FROM #새벽기도회
WHERE contains(file.name, "민수기")
SORT file.name
```
````

---

#### 예시 4: 링크 통계 (제텔카스텐 건강도)

````markdown
```dataview
TABLE length(file.outlinks) as "외부링크", length(file.inlinks) as "백링크"
FROM "3.Permanent_Notes"
SORT length(file.outlinks) DESC
```
````

---

### 1.4 실전 활용: 자동 업데이트 인덱스

**새벽기도회 인덱스에 추가**:

````markdown
## 📊 최근 10개 설교 (자동 업데이트)

```dataview
TABLE WITHOUT ID
  file.link as "설교",
  regexreplace(file.name, ".*(\d{6}).*", "$1") as "날짜",
  regexreplace(file.name, ".* (마태복음|민수기|고린도후서).*", "$1") as "성경책"
FROM "4.Prolific_Lounge/설교/새벽기도회"
SORT file.name DESC
LIMIT 10
```

## 📈 성경책별 통계

```dataview
TABLE length(rows) as "편수"
FROM "4.Prolific_Lounge/설교/새벽기도회"
WHERE contains(file.name, "마태복음") OR contains(file.name, "민수기") OR contains(file.name, "고린도후서")
GROUP BY regexreplace(file.name, ".* (마태복음|민수기|고린도후서).*", "$1") as "성경책"
SORT length(rows) DESC
```
````

---

## 📦 2. Templater 플러그인 ⭐⭐⭐

### 2.1 설치 방법

1. **탐색** → **"Templater"** 검색
2. **설치** → **활성화**

### 2.2 기본 설정

**설정** → **Templater**:

1. **Template folder location**:
   - `📁 9. 첨부파일/Templates`

2. **Trigger Templater on new file creation**: ✅ 활성화

3. **Folder Templates** 설정:
   - `4.Prolific_Lounge/설교/새벽기도회` → `설교_템플릿.md`
   - `4.Prolific_Lounge/묵상/선린단상` → `에세이_템플릿.md` (만들 경우)
   - `3.Permanent_Notes` → `영구메모_템플릿.md` (만들 경우)

### 2.3 템플릿 예시

#### 예시 1: 날짜 자동 입력

**설교 템플릿에 추가**:
```markdown
---
date: <% tp.date.now("YYYY-MM-DD") %>
---

# [<% tp.file.title %>]
```

**사용 시**:
- 파일 생성하면 자동으로 오늘 날짜 입력됨

---

#### 예시 2: 대화형 템플릿

**새 설교 템플릿**:
```markdown
<%*
let category = await tp.system.suggester(
  ["새벽", "청소년", "주일", "금요", "수요성경공부"],
  ["[새벽]", "[청소년]", "[주일]", "[금요]", "[수요성경공부]"]
);
let date = tp.date.now("YYMMDD");
let title = await tp.system.prompt("설교 제목");
let scripture = await tp.system.prompt("본문 (예: 마태복음 6:22-23)");

tR = `${category} ${date} ${title} ${scripture}`;
%>

# <% title %>
## <% scripture %> <% category %> 설교

---

[설교 내용 시작]
```

**사용 시**:
1. 새 파일 생성
2. 카테고리 선택 (드롭다운)
3. 제목 입력 (프롬프트)
4. 본문 입력 (프롬프트)
5. 자동으로 파일명과 내용 생성!

---

#### 예시 3: 월간 리뷰 자동화

**월간 리뷰 템플릿에 추가**:
```markdown
# 📅 <% tp.date.now("YYYY년 MM월") %> 창작작업장 월간 리뷰

> 작성일: <% tp.date.now("YYYY-MM-DD") %>

## 📊 1. 이번 달 생산량 확인

<%*
let folder = "4.Prolific_Lounge";
let files = app.vault.getMarkdownFiles()
  .filter(f => f.path.includes(folder))
  .filter(f => f.stat.ctime >= tp.date.now("x", "P-1M"));

tR = `총 ${files.length}개 파일 작성`;
%>
```

---

### 2.4 단축키 설정

**설정** → **단축키** → Templater 검색:

- **Templater: Insert template**: `Ctrl/Cmd + T`
- **Templater: Create new note from template**: `Ctrl/Cmd + Shift + N`

---

## 📦 3. Calendar 플러그인 ⭐⭐

### 3.1 설치 및 활성화

1. **탐색** → **"Calendar"** 검색
2. **설치** → **활성화**

### 3.2 사용법

**우측 사이드바에 달력 표시**:
- 날짜 클릭 → 그날의 노트로 이동 또는 생성
- 파일이 있는 날짜는 점(•)으로 표시

### 3.3 설정

**설정** → **Calendar**:
- **Daily note folder**: `📁 1.Fleeting_Notes/Daily` (또는 원하는 위치)
- **Week starts on**: `Monday`
- **Show week number**: ✅

### 3.4 활용 예시

**설교 일정 관리**:
- 2025-10-17: 새벽 설교 작성 완료 (점 표시)
- 2025-10-20: 청소년 설교 작성 예정
- 2025-10-31: 월간 리뷰 날짜

**시각적 확인**:
- 빈 날짜 확인 → 설교 준비 필요
- 밀집된 날짜 → 생산적인 주간

---

## 📦 4. Tag Wrangler 플러그인 ⭐⭐

### 4.1 설치 및 활성화

1. **탐색** → **"Tag Wrangler"** 검색
2. **설치** → **활성화**

### 4.2 사용법

**좌측 사이드바** → **태그 패널**:
- 태그 우클릭 → 옵션 표시
  - **Rename**: 태그명 일괄 변경
  - **Merge**: 태그 병합
  - **Delete**: 태그 일괄 삭제

### 4.3 실전 활용

#### 예시 1: 태그 통합

**문제**: `#새벽기도회`, `#새벽`, `#dawn` 혼재

**해결**:
1. `#새벽` 우클릭 → **Merge tags**
2. `#새벽기도회` 선택
3. 모든 `#새벽` → `#새벽기도회`로 일괄 변경

#### 예시 2: 태그 이름 변경

**문제**: `#설교` → `#설교/새벽`로 구조화하고 싶음

**해결**:
1. `#설교` 우클릭 → **Rename tag**
2. `#설교/새벽`로 변경
3. 모든 파일 자동 업데이트

---

## 📦 5. Recent Files 플러그인 ⭐

### 5.1 설치 및 활성화

1. **탐색** → **"Recent Files"** 검색
2. **설치** → **활성화**

### 5.2 사용법

**좌측 사이드바** → **최근 파일 아이콘**:
- 최근 10-20개 파일 목록
- 클릭하면 즉시 열림

### 5.3 설정

**설정** → **Recent Files**:
- **Number of recent files to show**: `20`
- **Show file path**: ✅
- **Omit path for daily notes**: ✅

---

## 🔧 종합 워크플로우

### 시나리오 1: 새 설교 작성

1. **Calendar**로 날짜 확인
2. **Templater** 단축키 (`Cmd+Shift+N`)
3. 설교 템플릿 선택
4. 카테고리/제목/본문 입력 → 자동 생성
5. 설교 작성
6. **저장하면 자동으로 인덱스에 추가** (Dataview)

**소요 시간**: 1분 (템플릿 사용 전: 5-10분)

---

### 시나리오 2: 월간 리뷰

1. **Templater**로 월간 리뷰 템플릿 실행
2. **Dataview**가 자동으로 이번 달 파일 개수 계산
3. 반복 주제 직접 작성
4. **Dataview**가 링크 통계 생성
5. 리뷰 완성

**소요 시간**: 30분 → 20분으로 단축

---

### 시나리오 3: 설교 검색

1. **Dataview** 쿼리로 특정 본문 검색
   ```dataview
   LIST
   FROM "4.Prolific_Lounge"
   WHERE contains(file.name, "마태복음 6")
   ```
2. 결과 즉시 확인
3. 클릭하여 열기

**소요 시간**: 5초 (수동 검색: 2-3분)

---

## 📊 효과 측정

### Before (플러그인 없음)

| 작업 | 소요 시간 |
|------|----------|
| 새 설교 파일 생성 | 5-10분 |
| 인덱스 수동 업데이트 | 10-15분 |
| 과거 설교 검색 | 2-5분 |
| 월간 리뷰 | 40-50분 |
| **합계 (월 1회)** | **약 60-80분** |

### After (플러그인 사용)

| 작업 | 소요 시간 | 절감 |
|------|----------|------|
| 새 설교 파일 생성 | 1분 | -90% |
| 인덱스 자동 업데이트 | 0분 | -100% |
| 과거 설교 검색 | 5초 | -98% |
| 월간 리뷰 | 20-30분 | -40% |
| **합계 (월 1회)** | **약 20-30분** | **-62%** |

**시간 절약**: 월 30-50분, 연간 6-10시간!

---

## ⚠️ 주의사항

### 1. 과도한 플러그인 설치 금지
- 필요한 것만 설치
- 사용하지 않는 플러그인은 비활성화
- 너무 많으면 Obsidian 느려짐

### 2. 백업
- 플러그인 설정 전 반드시 볼트 백업
- iCloud/OneDrive 자동 백업 권장

### 3. 버전 호환성
- Obsidian 업데이트 후 플러그인 호환성 확인
- 문제 발생 시 플러그인 재설치

### 4. 학습 곡선
- Dataview: 쿼리 언어 배우기 (1-2시간)
- Templater: JavaScript 기본 (1-2시간)
- 점진적으로 복잡한 기능 사용

---

## 📚 추가 학습 자료

### Dataview 공식 문서
- https://blacksmithgu.github.io/obsidian-dataview/

### Templater 공식 문서
- https://silentvoid13.github.io/Templater/

### Obsidian 커뮤니티 포럼
- https://forum.obsidian.md/

### YouTube 튜토리얼 (한글)
- 검색어: "Obsidian Dataview 한글"
- 검색어: "Obsidian Templater 강의"

---

## ✅ 설치 체크리스트

설치 후 이 체크리스트를 완료하세요:

- [ ] **Dataview 설치** 및 활성화
- [ ] Dataview 설정: JavaScript 쿼리 활성화
- [ ] 새벽기도회 인덱스에 Dataview 쿼리 추가
- [ ] Dataview 쿼리 정상 작동 확인

- [ ] **Templater 설치** 및 활성화
- [ ] Templater 템플릿 폴더 지정
- [ ] 설교 템플릿 폴더 연결
- [ ] 테스트 파일 생성으로 작동 확인

- [ ] **Calendar 설치** 및 활성화 (선택)
- [ ] Calendar 설정: 주간 시작일 월요일
- [ ] 우측 사이드바에 달력 확인

- [ ] **Tag Wrangler 설치** 및 활성화 (선택)
- [ ] 태그 패널에서 우클릭 가능 확인

- [ ] **Recent Files 설치** 및 활성화 (선택)
- [ ] 최근 파일 20개 표시 설정

- [ ] **전체 시스템 테스트**:
  - [ ] 새 설교 파일 생성 (Templater)
  - [ ] 인덱스 자동 업데이트 확인 (Dataview)
  - [ ] 검색 쿼리 작동 확인 (Dataview)

---

**설정 완료일**: __________

**다음 점검일**: __________ (3개월 후)

---

#Obsidian #플러그인 #Dataview #Templater #자동화 #가이드 #제텔카스텐
