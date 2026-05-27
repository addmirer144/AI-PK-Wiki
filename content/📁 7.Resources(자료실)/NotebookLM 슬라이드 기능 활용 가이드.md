## NotebookLM 슬라이드 기능 활용 가이드

NotebookLM은 Google이 개발한 AI 기반 연구 및 문서 정리 도구로, 최근 슬라이드 자동 생성(Slide Deck) 기능이 추가되면서 프레젠테이션 제작 효율성이 크게 향상되었습니다[1][2]. 업로드한 문서를 분석하여 완성도 높은 슬라이드를 자동으로 생성하며, 목회 및 교육 현장에서 특히 유용하게 활용할 수 있습니다[3][4].

### 슬라이드 생성 기능 개요

NotebookLM의 슬라이드 기능은 사용자가 업로드한 PDF, Google Docs, 웹페이지, YouTube 영상 등 다양한 소스를 분석하여 구조화된 프레젠테이션을 자동 생성합니다[1][2]. 생성된 슬라이드는 PDF로 다운로드하거나 링크로 공유할 수 있으며, NotebookLM 내에서 직접 전체화면 슬라이드쇼로 발표할 수도 있습니다[1].

**주요 특징:**
- 18세 이상 사용자에게 제공되는 기능[1]
- 백그라운드 생성 방식으로 다른 작업과 병행 가능[1]
- 다이어그램, 인용문, 데이터 등을 자동으로 추출하여 시각화[5][6]
- 최대 50개의 소스를 기반으로 슬라이드 생성 가능[7]

### 슬라이드 생성 단계별 가이드

**1단계: 노트북 생성 및 소스 업로드**

NotebookLM에 접속하여 새 노트북을 생성한 후, 프레젠테이션에 필요한 자료를 업로드합니다[3][8]. 지원되는 파일 형식은 PDF, TXT, Markdown, Google Docs/Slides, 오디오(mp3), 웹 URL, YouTube 링크 등 매우 다양합니다[8][9].

**2단계: Studio 패널에서 Slide Deck 선택**

오른쪽 Studio 패널에서 "Slide Deck" 옵션을 클릭하면 슬라이드 생성이 시작됩니다[1]. 바로 생성할 수도 있고, 연필 아이콘을 눌러 커스터마이징 옵션을 먼저 설정할 수도 있습니다[1].

**3단계: 슬라이드 커스터마이징 설정**

슬라이드 생성 전에 다음 사항을 맞춤 설정할 수 있습니다[1][10]:

**포맷 선택:**
- **Detailed Deck (상세 덱)**: 전체 텍스트와 세부 정보가 포함된 포괄적인 슬라이드로, 이메일 전송이나 독립적으로 읽기에 적합[1]
- **Presenter Slides (발표자 슬라이드)**: 깔끔하고 시각적인 슬라이드로 핵심 포인트만 담아 발표 시 활용[1]

**언어 선택:**
- 80개 이상의 언어 지원으로 한국어를 비롯한 다양한 언어로 슬라이드 생성 가능[7][10]

**길이 지정:**
- Short (짧게), Default (기본), Long (길게) 중 선택[1]

**프롬프트 입력 (가장 중요):**
슬라이드의 방향성을 구체적으로 지시하는 프롬프트를 입력합니다[1][10]. 개요, 대상 청중, 스타일, 초점을 명시하면 더욱 정확한 결과를 얻을 수 있습니다[1][10].

### 실전 프롬프트 예시

NotebookLM 슬라이드 기능의 핵심은 명확하고 구체적인 프롬프트 작성입니다. 다음은 목회 및 교육 현장에서 바로 활용할 수 있는 프롬프트 예시입니다.

**교회 교육용 슬라이드 제작:**

```
초등부 어린이를 대상으로 '탕자의 비유'(누가복음 15:11-32)를 이해하기 쉽게 설명하는 슬라이드를 만들어 주세요. 
각 슬라이드마다 핵심 교훈을 한 문장으로 요약하고, 어린이가 공감할 수 있는 현대적 예시를 포함해 주세요. 
밝고 친근한 스타일로 작성하며, 참여형 질문을 2-3개 포함해 주세요.
```


**설교 준비용 슬라이드:**

```
요한복음 3장 16절을 중심으로 20분 분량의 설교용 슬라이드를 작성해 주세요. 
서론-본론(3가지 핵심 메시지)-결론 구조로 구성하고, 각 핵심 메시지마다 성경적 해설과 현대 적용 예화를 포함해 주세요. 
장년 성도 대상이며, 정중하면서도 은혜로운 어조로 작성해 주세요.
```


**학습 자료용 슬라이드:**

```
업로드한 신학 논문의 핵심 내용을 신학생을 위한 10장짜리 학습 슬라이드로 만들어 주세요. 
각 슬라이드는 제목, 핵심 개념 정리(3-5개 bullet points), 관련 성경 구절을 포함하며, 
학문적이면서도 이해하기 쉬운 언어로 작성해 주세요.
```


**보고서 및 브리핑용 슬라이드:**

```
분기 사역 보고서를 경영진에게 발표할 5장짜리 슬라이드를 만들어 주세요. 
1장: 문제 정의 및 최근 동향, 2-3장: 핵심 패턴 및 성과 지표, 4장: 실행 아이디어, 5장: 다음 단계 계획. 
간결하고 전문적인 어조로 작성하며, 핵심 수치를 강조해 주세요.
```


**초보자 대상 교육용 슬라이드:**

```
초보자를 위해 단계별 설명이 포함된 슬라이드를 만들어 주세요. 
대담하고 재미있는 스타일을 사용하며, 각 단계마다 구체적인 실행 지침을 제공해 주세요.
```


**비교 분석 슬라이드:**

```
업로드한 자료를 바탕으로 세 가지 접근 방식(A, B, C)을 비교하는 슬라이드를 만들어 주세요. 
복잡성, 비용, 시간 투자, 최적 사용 사례 등의 주요 요소를 비교하는 표 형식을 포함해 주세요.
```


### 효과적인 프롬프트 작성 공식

NotebookLM에서 최상의 결과를 얻기 위해서는 프롬프트에 다음 요소를 포함하는 것이 중요합니다[11][12]:

**1. 맥락 (Context)**: 자신의 역할이나 배경 설명
- 예: "나는 청년부를 담당하는 목회자입니다"

**2. 상황 (Situation)**: 현재 상황과 해결하려는 문제
- 예: "다음 주일 청년부 예배를 위한 발표 자료를 준비 중입니다"

**3. 목적 (Purpose)**: 슬라이드의 구체적인 목적
- 예: "청년들이 성경의 핵심 메시지를 쉽게 이해하고 삶에 적용할 수 있도록 돕고 싶습니다"

**4. 출력 양식 (Format)**: 원하는 슬라이드 구조와 스타일
- 예: "10장 분량, 각 슬라이드당 3-5개 bullet points, 친근하고 대화체 어조"

### Video Overview 기능과의 연계 활용

NotebookLM의 Video Overview 기능은 업로드한 자료를 나레이션이 포함된 슬라이드 영상으로 자동 변환해 줍니다[5][6][13]. 이 기능을 슬라이드 생성과 함께 활용하면 더욱 풍부한 콘텐츠를 제작할 수 있습니다.

**커스터마이징 옵션:**[13][7][10]
- **포맷**: Explainer (심층 설명형) vs Brief (간략 요약형)
- **언어**: 80개 이상 언어 지원
- **비주얼 스타일**: Classic, Whiteboard, Watercolor, Retro Print, Heritage, Paper-craft, Kawaii, Anime 등 8가지 스타일 (18세 이상)
- **Steering Prompt**: 특정 소스나 주제에 집중하도록 지시

**Video Overview 프롬프트 예시:**[10][14]

```
이 신학 자료를 미국 오순절 교단에 관심 있는 청년 성도들을 위한 15분 분량의 교육 영상으로 만들어 주세요. 
영어 원문을 한국어로 번역하고, 주요 신학적 개념을 쉽게 설명하며, 
대화형 팟캐스트 스타일로 제작해 주세요.
```


### 생성된 슬라이드 관리 및 활용

**슬라이드 관리 기능:**[1]
- 이름 변경, PDF 다운로드, 공유, 삭제 등 세 점 메뉴에서 가능
- 생성 시 사용한 프롬프트 확인: "View custom prompt" 선택
- 전체화면 슬라이드쇼 모드: "Start slideshow" 선택

**공유 방법:**[1]
1. **링크 공유**: 슬라이드 링크를 복사하여 공유 (노트북 공유 설정 필요)
2. **노트북 전체 공유**: 다른 사용자가 Studio 패널에서 슬라이드 접근 가능
3. **PDF 다운로드 후 공유**: 다운로드한 PDF 파일을 직접 전송

### 실전 활용 시나리오

**시나리오 1: 주일학교 교육 자료 제작**[4]

1. 성경 본문과 교육 관련 자료를 NotebookLM에 업로드
2. 연령대별(유치부, 초등부, 중고등부) 맞춤 프롬프트 작성
3. Presenter Slides 포맷으로 시각적 슬라이드 생성
4. Video Overview로 나레이션 영상 추가 제작
5. PDF 다운로드 후 교사들에게 배포

**시나리오 2: 설교 자료 준비**[15][4]

1. 주석서, 관련 논문, 예화 자료 등을 소스로 업로드
2. 설교 구조(서론-본론-결론)를 명시한 프롬프트 입력
3. Detailed Deck 포맷으로 상세한 설교 노트 생성
4. AI가 제시한 구조를 기반으로 실제 설교문 작성
5. 필요시 Presenter Slides로 재생성하여 발표용으로 활용

**시나리오 3: 사역 보고 및 기획**[16][11]

1. 사역 관련 회의록, 보고서, 통계 자료 업로드
2. 경영진/당회 대상 브리핑 슬라이드 프롬프트 작성
3. 핵심 성과 지표와 향후 계획을 강조하는 슬라이드 생성
4. 슬라이드쇼 모드로 직접 발표하거나 PDF로 배포

**시나리오 4: 신학 강의 및 세미나**[14]

1. 영문 신학 자료를 PDF로 업로드
2. 한국어 번역 및 학습자 수준에 맞는 설명 요청
3. 학습 순서에 따른 구조화된 슬라이드 생성
4. Audio Overview 기능으로 팟캐스트 형식의 학습 자료 추가 제작

### 추가 실전 팁

**소스 준비 시:**[3][17][18]
- 파일명을 명확하게 정리하면 AI의 이해도와 인용 정확도가 향상됩니다
- 긴 문서는 챕터 단위로 나누어 업로드하면 더 정밀한 결과를 얻을 수 있습니다
- 한글 PDF보다 Google Docs 포맷이 AI가 더 잘 인식합니다

**프롬프트 작성 시:**[15][11][12]
- 구체적일수록 좋은 결과가 나옵니다
- 대상 청중을 명확히 명시하세요
- 원하는 슬라이드 수를 지정하세요
- 스타일과 어조(formal, casual, academic 등)를 지정하세요

**결과 개선 방법:**[3][15]
- 첫 결과가 만족스럽지 않다면 프롬프트를 수정하여 재생성하세요
- "이 답변의 근거 문장도 알려줘"라고 추가 질문하여 출처를 확인하세요
- 생성된 슬라이드를 채팅 기능으로 수정 요청할 수 있습니다

**Gemini와 연계 활용:**[19]

NotebookLM에서 생성한 개요를 Google Gemini의 Canvas 기능으로 가져가면 더욱 시각적으로 풍부한 PowerPoint 프레젠테이션을 만들 수 있습니다[19]. NotebookLM의 연구 능력과 Gemini의 디자인 능력을 결합하는 워크플로우입니다.

### 무료 vs 유료 (NotebookLM Plus) 비교

|기능|무료 버전|NotebookLM Plus|
|---|---|---|
|슬라이드 생성 기능|가능|가능|
|생성 가능한 노트북 수|제한적|최대 5배 확장|
|어조/스타일 조정|제한적|고급 커스터마이징 가능|
|협업 및 공유|기본 기능|팀 협업 강화|
|역할 기반 설정|불가능|AI 역할 지정 가능|

[20][21][22]

NotebookLM의 슬라이드 기능은 목회자, 교육자, 연구자에게 강력한 도구입니다. 명확한 프롬프트와 체계적인 소스 준비를 통해 시간을 크게 절약하고 퀄리티 높은 프레젠테이션을 제작할 수 있습니다[3][23][24].

출처
[1] Generate a Slide Deck in NotebookLM https://support.google.com/notebooklm/answer/16757456
[2] NotebookLM 알아보기 - 컴퓨터 https://support.google.com/notebooklm/answer/16164461?hl=ko&co=GENIE.Platform%3DDesktop
[3] NotebookLM Prompts Guide: Effortless AI Slide Creation For ... https://moiid.com/en/effortless-presentation-slides-how-to-use-notebooklm-prompts-for-fast-ai-powered-decks/
[4] 목회자를 위한 챗GPT 프롬프트 10선 https://brunch.co.kr/@morningwalk/1230
[5] Google's NotebookLM Can Now Turn Your Notes Into ... https://www.pcmag.com/news/googles-notebooklm-can-now-turn-your-notes-into-narrated-slideshows
[6] NotebookLM updates: Video Overviews, Studio upgrades https://blog.google/technology/google-labs/notebooklm-video-overviews-studio-upgrades/
[7] NotebookLM Rolls Out Customizable Video Overviews For ... https://www.timesofai.com/news/customizable-video-overviews-in-notebooklmfully-rolls-out/
[8] NotebookLM 사용법 및 활용 - 아카이브러리 https://memo0800.tistory.com/entry/NotebookLM-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%B0%8F-%ED%99%9C%EC%9A%A9
[9] 내 자료만 학습하는 AI 비서, NotebookLM 사용법 완벽 가이드 ... https://peekaboolabs.ai/blog/notebooklm-ai-assistant-guide
[10] Generate Video Overviews in NotebookLM https://support.google.com/notebooklm/answer/16454555?hl=en
[11] 노트북LM으로 팀 결과물 관리하는 마케팅 팀장의 실전 활용법 4 ... https://peekaboolabs.ai/blog/notebooklm-marketing-team-productivity
[12] AI로 10배 빠른 리서치: 가장 친절한 NotebookLM 사용법 A to Z https://maily.so/airecipe/posts/xyowme93z28
[13] How to customise NotebookLM Video Overviews https://www.youtube.com/watch?v=5RX7V7iplsA
[14] [왕초보 AI사용팁] 구글 notebookLM으로 신학 컨텐츠 뚝딱! ... https://www.youtube.com/watch?v=Dw9Eo_7Gy3c
[15] 리서치부터 글쓰기까지 한 번에: NotebookLM - 문장의 정원 https://bolsulog.com/entry/%EB%A6%AC%EC%84%9C%EC%B9%98%EB%B6%80%ED%84%B0-%EA%B8%80%EC%93%B0%EA%B8%B0%EA%B9%8C%EC%A7%80-%ED%95%9C-%EB%B2%88%EC%97%90-NotebookLM
[16] [NotebookLM 사용법 1] 연구 아티클 10편으로 만드는 '한 ... https://tilnote.io/pages/6906285b798cbff383bda6db
[17] NotebookLM: A Guide With Practical Examples https://www.datacamp.com/tutorial/notebooklm
[18] How to Use NotebookLM: Create Study Notes & ... https://www.codecademy.com/article/how-to-use-notebooklm
[19] NotebookLM + Gemini Will Create Stunning AI Slides for ... https://www.youtube.com/watch?v=Hjj5Z-zblWQ
[20] 초보자도 쉽게 따라하는 NotebookLM 사용법 완전정복! - ITMEN https://itmen.tistory.com/300
[21] NotebookLM: 정보 과잉 시대를 위한 이해 중심 AI 요약 도우미 https://joonfluence.tistory.com/880
[22] 구글 노트북 LM 완벽 가이드 https://brunch.co.kr/@jaylep/123
[23] Paul - notebooklm으로 딸깍 클릭으로 만든 슬라이드 ... https://www.facebook.com/photo.php?fbid=3561848363949571&set=a.618477948286642&type=3
[24] 바쁜 목회자를 위한 하루 10분 투자…'AI 비서' 활용법 http://www.igoodnews.net/news/articleView.html?idxno=81712
[25] 구글이 랩탑LM 업데이트를 냈는데, 완전한 콘텐츠 제작 ... https://www.reddit.com/r/ThinkingDeeplyAI/comments/1oe8xx2/google_just_dropped_notebooklm_updates_that_turn/
[26] 업무에 Notebook LM을 사용하는 방법 https://clickup.com/ko/blog/266978/how-to-use-notebooklm-for-work
[27] 드디어 슬라이드 생성 기능이 노트북LM에 추가됨! 비디오 ... https://x.com/mahler83/status/1991668493612454222
[28] The Ultimate Guide to NotebookLM - All 2025 Features ... https://www.youtube.com/watch?v=FOs4RDTC52Q
[29] AI 비서가 내 문서를 요약해준다? 구글 NotebookLM 완전 정복 ... https://peopleware.tistory.com/54
[30] Tutorial - Google Notebook LM https://sites.google.com/view/notebook-lm/tutorial
[31] This Rumored Feature Could Make NotebookLM Essential ... https://www.askedtech.com/knowledge-archive/6900496eb7aa20b3946d5cb0
[32] 나만의 AI 연구 비서, Google NotebookLM 완벽 가이드 https://pointer81.tistory.com/entry/%EB%82%98%EB%A7%8C%EC%9D%98-AI-%EC%97%B0%EA%B5%AC-%EB%B9%84%EC%84%9C-Google-NotebookLM-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C
[33] Google NotebookLM | AI Research Tool & Thinking Partner https://notebooklm.google
[34] Google Did It! How To Make AI Presentations For Free with ... https://www.youtube.com/watch?v=f_qWPgK1JZ8
[35] 노트북LM 하나로 '이것'만 해도 미친 결과 나온다! Google ... https://www.youtube.com/watch?v=57W8QzACSic
[36] Best prompts thread : r/notebooklm https://www.reddit.com/r/notebooklm/comments/1gt6v16/best_prompts_thread/
[37] 개발자용 NotebookLM 사용 방법 https://clickup.com/ko/blog/259370/how-to-use-notebooklm-for-developers
[38] My AI Smarteasy에서 프롬프트 작성하기 – 구글 ... http://www.umlcert.com/0802-03/
[39] How To Create Video Overviews & More NEW Features in ... https://www.youtube.com/watch?v=HM9BwicW7dQ
[40] A Complete How-To Guide to NotebookLM https://learnprompting.org/blog/notebooklm-guide
[41] Loving the New NotebookLM Feature - Video Overview https://www.reddit.com/r/notebooklm/comments/1mcivpj/loving_the_new_notebooklm_feature_video_overview/
[42] 9 Immediately Useful NotebookLM Prompts to Accelerate Your ... https://excellentprompts.substack.com/p/notebooklm
[43] 노트북LM 실전 활용법: 연구원의 업무 생산성을 10배 높이는 3 ... https://peekaboolabs.ai/blog/notebooklm-productivity-tips
[44] 목회자를 위해 세 시간씩 절약해주는 6가지 ChatGPT 프롬프트 https://www.toolify.ai/ko/ai-news-kr/6-chatgpt-744109
[45] 6 NotebookLM Prompts That Do Your Hard Work For You https://www.aifire.co/p/6-notebooklm-prompts-that-do-your-hard-work-for-you
[46] NotebookLM Got Crazy Powerful: Here's How I Used It to ... https://aimaker.substack.com/p/learn-ai-agents-notebooklm-customization-guide-video-podcast-flashcards-quiz
[47] 10 Deep Prompts I Use with NotebookLM to Get Layered, ... https://www.reddit.com/r/notebooklm/comments/1kjtr47/10_deep_prompts_i_use_with_notebooklm_to_get/
[48] Customize Notebook Responses | NotebookLM Course https://www.futurepedia.io/courses/google-notebooklm-complete-course/lessons/customize-the-style-and-length-of-your-notebook-responses
[49] Best customisation settings? : r/notebooklm https://www.reddit.com/r/notebooklm/comments/1g711yv/best_customisation_settings/
[50] NotebookLM으로 목사님의 설교말씀을 요약 정리하고 신앙 ... https://www.gpters.org/research/post/notebooklm-summarizes-pastors-sermons-ZgTCf38aHmiyZRS
[51] 3 NotebookLM prompts I use that practically make my ... https://www.xda-developers.com/notebooklm-prompts-to-make-presentation-slides/
[52] [왕초보 AI활용법] (더보기란에 자료공유) 성경연구,설교자가 ... https://www.youtube.com/watch?v=tYoc4daFcWs
[53] Learn 80% of NotebookLM in Under 13 Minutes! https://www.youtube.com/watch?v=EOmgC3-hznM
