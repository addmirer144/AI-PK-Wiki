---
title: "Claude Code in Action | Claude Code in Action"
source: "https://keunyoung.gitbook.io/claude-course/"
author:
published: 2026-03-07
created: 2026-03-10
description: "이 문서는 학습을 더 쉽게 하기 위해 만들어진 문서입니다."
tags:
  - "clippings"
---
> **출처:**[Anthropic Academy — Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

---

---

> **유형:** Video Lesson (38초) 이 코스는 네 개의 섹션으로 구성됩니다.**코스 목표**

- 코딩 어시스턴트란 무엇인가?
- 왜 Claude Code인가?
- Claude Code를 파트너로 활용하기
- Claude Code를 최대한 활용하는 방법

---

> **유형:** Video Lesson (5분 53초) 코딩 어시스턴트는 단순히 코드를 작성해 주는 도구 그 이상입니다. 언어 모델을 활용해 복잡한 프로그래밍 작업을 처리하는 정교한 시스템입니다. 어시스턴트가 내부적으로 어떻게 작동하는지 이해하면, 진정으로 강력한 코딩 파트너가 무엇인지 알 수 있습니다.

코딩 어시스턴트에게 에러 메시지를 기반으로 버그를 수정하는 것과 같은 작업을 맡기면, 어시스턴트는 숙련된 개발자가 문제를 해결하는 방식과 유사한 프로세스를 따릅니다.

- **컨텍스트 수집** — 에러가 무엇을 가리키는지, 코드베이스의 어느 부분이 영향을 받는지, 어떤 파일이 관련되어 있는지 파악
- **계획 수립** — 코드를 수정하고 테스트를 실행해 수정 사항을 검증하는 등 문제 해결 방법 결정
- **실행** — 파일을 업데이트하고 명령을 실행해 실제로 솔루션 구현

핵심은 첫 번째와 세 번째 단계에서 어시스턴트가 외부 세계와 상호작용해야 한다는 것입니다. 즉, 파일 읽기, 문서 조회, 명령 실행, 코드 편집 등의 작업이 필요합니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FIweR3R1t0rcNHXNideHu%2F002_%2520_What_is_a_Coding_Assistant%3F_02.1750967940100.png&width=768&dpr=3&quality=100&sign=c4d881c2&sv=2)

Coding Assistant Flow

여기서 흥미로운 점이 있습니다. 언어 모델 자체는 텍스트를 처리하고 텍스트를 반환하는 것만 할 수 있습니다. 실제로 파일을 읽거나 명령을 실행할 수는 없습니다. 독립적인 언어 모델에게 파일을 읽어달라고 하면, 그런 기능이 없다고 답할 것입니다. 그렇다면 코딩 어시스턴트는 이 문제를 어떻게 해결할까요? 바로 **"툴 사용(tool use)"** 이라는 영리한 시스템을 활용합니다.

코딩 어시스턴트에 요청을 보내면, 어시스턴트는 언어 모델에게 특정 동작을 요청하는 방법을 알려주는 지시문을 자동으로 메시지에 추가합니다. 예를 들어, 다음과 같은 텍스트를 추가할 수 있습니다.

> *"파일을 읽고 싶다면, 'ReadFile: 파일명' 형식으로 응답하세요"*

전체 흐름은 다음과 같습니다.

1

사용자가 질문: *"main.go 파일에는 어떤 코드가 작성되어 있나요?"*

2

코딩 어시스턴트가 툴 지시문을 요청에 추가

3

언어 모델이 응답: *"ReadFile: main.go"*

4

코딩 어시스턴트가 실제 파일을 읽고 내용을 모델에 전달

5

언어 모델이 파일 내용을 바탕으로 최종 답변 제공

이 시스템 덕분에 언어 모델은 실제로는 형식화된 텍스트 응답을 생성하는 것임에도, 파일을 "읽고", 코드를 "작성하고", 명령을 "실행"할 수 있게 됩니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FwNW0j8Bg4T2roZLsQ5JY%2F002_%2520_What_is_a_Coding_Assistant%3F_14.1750967942536.png&width=768&dpr=3&quality=100&sign=7121fed5&sv=2)

Tool Use Flow Diagram

모든 언어 모델이 툴 사용에 동일하게 능숙하지는 않습니다. Claude 모델 시리즈(Opus, Sonnet, Haiku)는 특히 툴의 기능을 이해하고 복잡한 작업을 완수하기 위해 효과적으로 활용하는 능력이 뛰어납니다.

이러한 툴 사용 강점은 Claude Code에 다음과 같은 주요 이점을 제공합니다.

- **더 어려운 작업 처리** — Claude는 다양한 툴을 조합해 복잡한 작업을 처리하며, 이전에 보지 못한 툴도 활용할 수 있습니다.
- **확장 가능한 플랫폼** — Claude Code에 새로운 툴을 손쉽게 추가할 수 있으며, 워크플로우가 변화해도 Claude가 적응합니다.
- **향상된 보안** — Claude Code는 인덱싱 없이 코드베이스를 탐색할 수 있어, 전체 코드베이스를 외부 서버에 전송하지 않아도 됩니다.

#### 핵심 정리

- 코딩 어시스턴트는 언어 모델을 활용해 다양한 작업을 수행합니다.
- 언어 모델은 실제 프로그래밍 작업 대부분을 처리하기 위해 툴이 필요합니다.
- 모든 언어 모델이 동일한 수준으로 툴을 활용하지는 않습니다.
- Claude의 뛰어난 툴 사용 능력은 Claude Code에서 더 나은 보안, 커스터마이징, 지속성을 가능하게 합니다.

툴 사용 능력이야말로 단순한 텍스트 생성 모델을 파일을 읽고, 코드베이스를 이해하고, 프로젝트에 의미 있는 변경을 가할 수 있는 강력한 코딩 어시스턴트로 변환시키는 핵심입니다.

> **보충 설명:**
> 
> - **컨텍스트 윈도우(context window):** 언어 모델은 한 번에 처리할 수 있는 텍스트 양(토큰 수)에 한계가 있습니다. Claude Code는 대화가 길어질수록 이 한도에 가까워지며, 이것이 대화 기록 관리가 중요한 이유입니다 (Lesson 8 참고).
> - **반복 루프 동작:** Claude Code는 단일 툴 호출로 끝나지 않습니다. 목표를 달성할 때까지 "툴 호출 → 결과 확인 → 다음 판단"을 반복하는 루프(loop)로 동작합니다. 복잡한 작업일수록 이 루프가 여러 번 반복됩니다.

---

> **유형:** Video Lesson (8분 25초) Claude Code는 파일 읽기, 코드 작성, 명령 실행, 디렉토리 관리 등 일반적인 개발 작업을 처리하는 포괄적인 내장 툴 세트를 갖추고 있습니다. 하지만 Claude Code가 진정으로 강력한 이유는 이러한 툴들을 지능적으로 조합해 복잡하고 다단계 문제를 해결하는 능력에 있습니다.

---

---

> **유형:** Text Lesson 이제 로컬 환경에 Claude Code를 설치해 봅시다! 전체 설치 방법은 여기서 확인할 수 있습니다: https://code.claude.com/docs/en/quickstart

간략히 정리하면, 다음 단계가 필요합니다.

**Claude Code 설치**

- MacOS (Homebrew): `brew install --cask claude-code`
- MacOS, Linux, WSL: `curl -fsSL https://claude.ai/install.sh | bash`
- Windows CMD: `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd`

설치 후 터미널에서 `claude` 를 실행하세요. 처음 실행할 때 인증 과정을 거치게 됩니다.

> **보충 설명:**
> 
> - **사용 요금:** Claude Code는 **Claude Max 구독** 또는 **Anthropic API 키** 가 있어야 사용할 수 있습니다. 처음 `claude` 를 실행하면 브라우저 로그인 또는 API 키 입력을 안내받습니다.
> - **VS Code 사용자:** 터미널 대신 VS Code Extension으로도 Claude Code를 사용할 수 있습니다. VS Code 마켓플레이스에서 "Claude Code"를 검색해 설치하면 에디터 내에서 바로 사용 가능합니다.

AWS Bedrock 또는 Google Cloud Vertex를 사용하는 경우 추가 설정이 필요합니다.

- AWS Bedrock 특별 설정: https://code.claude.com/docs/en/amazon-bedrock
- Google Cloud Vertex 특별 설정: https://code.claude.com/docs/en/google-vertex-ai

---

> **유형:** Text Lesson 작업할 프로젝트가 있으면 Claude Code를 더 흥미롭게 활용할 수 있습니다. 이전 영상에서 소개된 UI 생성 앱과 동일한 소규모 프로젝트를 준비했습니다. **참고:** 반드시 이 프로젝트를 실행할 필요는 없습니다. 원하신다면 코스의 나머지 부분을 본인의 코드베이스로 진행하셔도 됩니다!

#### 설정 방법

이 프로젝트는 약간의 초기 설정이 필요합니다.

1

로컬 환경에 Node JS가 설치되어 있는지 확인하세요. [설치 안내 링크](https://nodejs.org/en/download)

2

이 강의에 첨부된 `uigen.zip` 파일을 다운로드하고 압축을 해제하세요.

3

프로젝트 디렉토리에서 `npm run setup` 을 실행해 의존성을 설치하고 로컬 SQLite 데이터베이스를 설정하세요.

4

이 프로젝트는 Anthropic API를 통해 Claude를 활용해 UI 컴포넌트를 생성합니다. 완전히 테스트하려면 API 키가 필요합니다. API 키가 없어도 앱은 정적인 가짜 코드를 생성합니다.

- Anthropic API 키 발급: https://console.anthropic.com/
- `.env` 파일에 API 키를 입력하세요.

5

`npm run dev` 를 실행해 프로젝트를 시작하세요.

---

> **유형:** Video Lesson Claude와 함께 코딩 프로젝트를 진행할 때 컨텍스트 관리는 매우 중요합니다. 프로젝트에는 수십 또는 수백 개의 파일이 있을 수 있지만, Claude가 효과적으로 도움을 주려면 적절한 정보만 있으면 됩니다. 관련 없는 컨텍스트가 너무 많으면 오히려 Claude의 성능이 저하되므로, 관련 파일과 문서 방향을 잘 안내하는 것이 중요합니다.

#### /init 명령

새 프로젝트에서 Claude를 처음 시작할 때 `/init` 명령을 실행하세요. 이 명령은 Claude가 전체 코드베이스를 분석하고 다음을 파악하도록 합니다.

- 프로젝트의 목적과 아키텍처
- 중요한 명령어와 핵심 파일
- 코딩 패턴과 구조

코드를 분석한 후 Claude는 요약본을 작성하고 `CLAUDE.md` 파일에 저장합니다. 파일 생성 권한을 요청하면 Enter를 눌러 개별 승인하거나, **Shift+Tab** 을 눌러 세션 동안 파일을 자유롭게 작성하도록 허용할 수 있습니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FNoAHNo5sbbdsVOQgsaw6%2F004_%2520_Adding_Context_02.1750967940092.png&width=768&dpr=3&quality=100&sign=67e02590&sv=2)

CLAUDE.md creation flow

#### CLAUDE.md 파일

`CLAUDE.md` 파일은 두 가지 주요 목적을 가집니다.

1. 중요한 명령어, 아키텍처, 코딩 스타일을 안내하며 Claude가 코드베이스를 파악하도록 도움
2. Claude에게 특정 또는 맞춤형 지시사항을 제공할 수 있도록 허용

이 파일은 Claude에 보내는 모든 요청에 포함되므로, 프로젝트 전용 지속적인 시스템 프롬프트처럼 작동합니다.

> **보충 설명:**
> 
> - **간결하게 유지하세요:** CLAUDE.md는 매 요청마다 컨텍스트에 포함되므로 너무 길면 오히려 성능이 저하됩니다. 핵심 정보만 담는 것이 중요합니다.
> - **다른 파일 import:**`@path/to/file.md` 형식으로 다른 마크다운 파일의 내용을 CLAUDE.md 안에서 불러올 수 있습니다. 긴 문서는 별도 파일로 분리하고 참조하는 방식이 효율적입니다.
> - **효과적인 CLAUDE.md 작성 팁:** 프로젝트 실행 명령(`npm run dev` 등), 주요 아키텍처 패턴, 팀 코딩 규칙, 자주 참조하는 파일 경로를 포함하면 Claude가 더 정확하게 도움을 줄 수 있습니다.

Claude는 세 가지 일반적인 위치에 있는 `CLAUDE.md` 파일을 인식합니다.

파일

설명

`CLAUDE.md`

`CLAUDE.local.md`

`~/.claude/CLAUDE.md`

`CLAUDE.md` 파일에 지시사항을 추가해 Claude의 동작을 커스터마이징할 수 있습니다. `#` 명령을 사용하면 "메모리 모드"로 진입해 `CLAUDE.md` 파일을 지능적으로 편집할 수 있습니다. 예를 들어 다음과 같이 입력하세요.

Claude가 이 지시사항을 `CLAUDE.md` 파일에 자동으로 병합합니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FNRsR9nyuqXELFEemb9LY%2F004_%2520_Adding_Context_05.1750967940882.png&width=768&dpr=3&quality=100&sign=75e6dbc3&sv=2)

Custom instructions in CLAUDE.md

특정 파일을 Claude에게 보여주고 싶을 때 `@` 기호 뒤에 파일 경로를 입력하면 해당 파일의 내용이 자동으로 요청에 포함됩니다. 예를 들어 다음과 같이 입력하세요.

```
How does the auth system work? @auth
```

Claude가 관련 파일 목록을 보여주고, 선택한 파일이 대화에 포함됩니다.

같은 `@` 문법을 사용해 `CLAUDE.md` 파일에서 직접 파일을 언급할 수도 있습니다. 예를 들어 다음과 같이 작성하세요.

```
The database schema is defined in the @prisma/schema.prisma file.

Reference it anytime you need to understand the structure of data stored in the database.
```

이렇게 파일을 언급하면 해당 파일의 내용이 모든 요청에 자동으로 포함됩니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F8eVQEE6ms7LPHbtZaoSZ%2F004_%2520_Adding_Context_09.1750967941793.png&width=768&dpr=3&quality=100&sign=66c752ce&sv=2)

File mention with @ syntax

---

> **유형:** Video Lesson 개발 환경에서 Claude와 작업할 때 기존 프로젝트에 변경 사항을 적용해야 하는 경우가 많습니다. 이 가이드에서는 스크린샷을 통한 시각적 커뮤니케이션과 Claude의 고급 추론 기능을 활용하는 등 변경 사항을 효과적으로 구현하는 실용적인 기법을 다룹니다.

Claude와 소통하는 가장 효과적인 방법 중 하나는 스크린샷을 활용하는 것입니다. 인터페이스의 특정 부분을 수정하고 싶을 때 스크린샷을 찍으면 Claude가 정확히 무엇을 가리키는지 이해하는 데 도움이 됩니다.

> 스크린샷을 Claude에 붙여넣으려면 macOS의 Cmd+V가 아닌 **Ctrl+V** 를 사용하세요. 이미지를 붙여넣은 후 애플리케이션의 해당 영역에 대한 구체적인 변경 사항을 요청할 수 있습니다.

코드베이스 전반에 걸쳐 광범위한 조사가 필요한 복잡한 작업에는 플래닝 모드를 활성화할 수 있습니다. 이 기능을 사용하면 Claude가 변경 사항을 구현하기 전에 프로젝트를 철저하게 탐색합니다.

**Shift + Tab을 두 번** 누르면 플래닝 모드가 활성화됩니다(자동 편집 승인 상태라면 한 번). 이 모드에서 Claude는 다음을 수행합니다.

- 프로젝트의 더 많은 파일 읽기
- 상세한 구현 계획 작성
- 수행할 내용을 정확히 보여주기
- 진행 전 사용자 승인 대기

이를 통해 계획을 검토하고 Claude가 중요한 사항을 놓쳤거나 특정 시나리오를 고려하지 않은 경우 방향을 수정할 수 있습니다.

Claude는 "씽킹(thinking)" 모드를 통해 다양한 수준의 추론을 제공합니다. 이를 통해 솔루션을 제공하기 전에 복잡한 문제를 더 깊이 생각하는 시간을 가질 수 있습니다.

모드

설명

"Think"

기본 추론

"Think more"

확장된 추론

종합적 추론

"Think longer"

"Ultrathink"

각 모드는 Claude에게 점진적으로 더 많은 토큰을 할당해 어려운 문제에 대한 더 깊은 분석을 가능하게 합니다.

기능

최적 활용 상황

**플래닝 모드**

**씽킹 모드**

두 모드를 함께 사용하면 폭넓은 이해와 깊이 있는 분석이 모두 필요한 작업을 처리할 수 있습니다. 두 기능 모두 추가 토큰을 소모한다는 점을 유의하세요.

---

> **유형:** Video Lesson 복잡한 작업에서 Claude와 작업할 때 대화가 집중력을 유지하고 생산적으로 진행되도록 안내해야 할 경우가 많습니다. 대화의 흐름을 제어하고 Claude가 올바른 방향을 유지하도록 도움을 주는 몇 가지 기법이 있습니다.

Claude가 잘못된 방향으로 가거나 너무 많은 것을 한꺼번에 처리하려 할 때 **Escape** 키를 눌러 응답 중간에 멈출 수 있습니다. 이를 통해 대화의 방향을 수정할 수 있습니다. 특히 Claude가 여러 작업을 동시에 처리하려 할 때 특정 한 가지 작업에만 집중하도록 유도할 때 유용합니다.

Escape 기법의 가장 강력한 활용법 중 하나는 반복적인 오류를 수정하는 것입니다. Claude가 여러 대화에서 같은 실수를 반복할 때 다음과 같이 처리할 수 있습니다.

1

Escape를 눌러 현재 응답 중단

2

`#` 단축키를 사용해 올바른 접근 방식에 대한 메모리 추가

3

수정된 정보로 대화 계속

이렇게 하면 프로젝트의 이후 대화에서 Claude가 같은 오류를 반복하지 않습니다.

#### 대화 되감기

긴 대화를 진행하다 보면 관련 없거나 혼란을 줄 수 있는 컨텍스트가 쌓일 수 있습니다. **Escape를 두 번** 누르면 대화를 되감을 수 있습니다. 지금까지 보낸 모든 메시지가 표시되고, 이전 시점으로 돌아가 대화를 계속할 수 있습니다.

명령어

사용 시점

`/compact`

`/clear`

Escape, Escape 두 번, `/compact`, `/clear` 를 전략적으로 활용하면 개발 워크플로우 전반에서 Claude의 집중력과 생산성을 유지할 수 있습니다.

> **보충 설명 — 컨텍스트 오염(Context Poisoning):** 대화가 길어지면 Claude의 응답 품질이 점점 떨어지는 현상을 경험할 수 있습니다. 이는 대화 초반에 Claude가 잘못 인식한 내용이나 오류가 이후 모든 응답의 바탕이 되기 때문입니다. 이를 **컨텍스트 오염** 이라고 합니다.
> 
> 이것이 단순히 "틀린 답변을 수정해줘"라고 하는 것보다 **Escape 두 번으로 되감기** 가 더 강력한 이유입니다. 되감기는 잘못된 정보가 포함된 컨텍스트 자체를 제거해 오염 이전 상태로 돌아갑니다.
> 
> 실용적 가이드:
> 
> - 같은 기능 작업을 계속할 때 → `/compact` (핵심 정보 유지)
> - Claude 응답이 점점 이상해질 때 → Escape 두 번으로 되감기
> - 완전히 다른 작업으로 전환할 때 → `/clear`

---

> **유형:** Video Lesson Claude Code에는 슬래시(/)를 입력해 접근할 수 있는 내장 명령어가 있으며, 자주 실행하는 반복 작업을 자동화하기 위한 커스텀 명령어를 직접 만들 수도 있습니다.

커스텀 명령어를 만들려면 프로젝트에 특정 폴더 구조를 설정해야 합니다.

1

프로젝트 디렉토리에서 `.claude` 폴더를 찾으세요.

2

그 안에 `commands` 디렉토리를 새로 만드세요.

3

원하는 명령어 이름으로 새 마크다운 파일을 만드세요(예: `audit.md`). 파일명이 명령어 이름이 됩니다. 즉, `audit.md` 를 만들면 `/audit` 명령어가 생성됩니다.

**커스텀 명령어 파일을 만든 후에는 Claude Code를 재시작해야 새 명령어를 인식합니다.**

> **보충 설명:**
> 
> - **글로벌 명령어:**`~/.claude/commands/` 디렉토리에 파일을 만들면 모든 프로젝트에서 공통으로 사용할 수 있는 글로벌 명령어가 됩니다. 같은 이름의 명령어가 있다면 프로젝트 명령어(`.claude/commands/`)가 글로벌보다 우선 적용됩니다.
> - **명령어 안에서 파일 참조:** 명령어 파일 내에서도 `@파일경로` 문법을 사용해 특정 파일의 내용을 포함시킬 수 있습니다. 예를 들어 코딩 규칙 문서를 참조하도록 명령어를 작성할 수 있습니다.

프로젝트 의존성의 취약점을 감사하는 커스텀 명령어의 실용적인 예시입니다. 이 audit 명령어는 세 가지 작업을 수행합니다.

1

`npm audit` 을 실행해 취약한 패키지 찾기

2

`npm audit fix` 를 실행해 업데이트 적용

3

업데이트로 인해 오류가 발생하지 않는지 테스트 실행

커스텀 명령어는 `$ARGUMENTS` 플레이스홀더를 사용해 인수를 받을 수 있습니다. 이를 통해 명령어를 훨씬 유연하고 재사용 가능하게 만들 수 있습니다. 예를 들어 `write_tests.md` 명령어에 다음과 같은 내용을 담을 수 있습니다.

```
Write comprehensive tests for: $ARGUMENTS

Testing conventions:

* Use Vitests with React Testing Library

* Place test files in a __tests__ directory in the same folder as the source file

* Name test files as [filename].test.ts(x)

* Use @/ prefix for imports

Coverage:

* Test happy paths

* Test edge cases

* Test error states
```

그런 다음 파일 경로와 함께 명령어를 실행할 수 있습니다.

```
/write_tests the use-auth.ts file in the hooks directory
```

#### 주요 이점

- **자동화** — 반복적인 워크플로우를 단일 명령어로 변환
- **일관성** — 매번 동일한 단계가 수행되도록 보장
- **컨텍스트** — 프로젝트별 지시사항과 규칙을 Claude에 제공
- **유연성** — 인수를 사용해 다양한 입력에 명령어 적용

---

> **유형:** Video Lesson MCP(Model Context Protocol) 서버를 추가해 Claude Code의 기능을 확장할 수 있습니다. 이 서버는 원격 또는 로컬 머신에서 실행되며 Claude에게 기본적으로 제공되지 않는 새로운 툴과 기능을 추가합니다. 가장 인기 있는 MCP 서버 중 하나는 **Playwright** 로, Claude가 웹 브라우저를 제어할 수 있게 해줍니다. 이를 통해 웹 개발 워크플로우에서 강력한 가능성이 열립니다.

Claude Code에 Playwright 서버를 추가하려면 터미널(Claude Code 내부가 아닌)에서 다음 명령을 실행하세요.

```
claude mcp add playwright npx @playwright/mcp@latest
```

이 명령은 두 가지를 수행합니다.

1. MCP 서버 이름을 "playwright"로 지정
2. 로컬 머신에서 서버를 시작하는 명령 제공

#### 권한 관리

MCP 서버 툴을 처음 사용할 때 Claude는 매번 권한을 요청합니다. 이 권한 요청이 번거롭다면, 설정을 편집해 서버를 미리 승인할 수 있습니다.

`.claude/settings.local.json` 파일을 열고 allow 배열에 서버를 추가하세요.

```
{

  "permissions": {

    "allow": ["mcp__playwright"],

    "deny": []

  }

}
```

> `mcp__playwright` 의 이중 밑줄에 주의하세요.

프롬프트를 수동으로 테스트하고 수정하는 대신, Claude에게 다음을 수행하도록 할 수 있습니다.

1

브라우저를 열고 애플리케이션으로 이동

2

테스트 컴포넌트 생성

3

시각적 스타일링과 코드 품질 분석

4

관찰한 내용을 바탕으로 생성 프롬프트 업데이트

5

새 컴포넌트로 개선된 프롬프트 테스트

예를 들어 Claude에게 다음과 같이 요청할 수 있습니다.

> *"localhost:3000으로 이동해 기본 컴포넌트를 생성하고, 스타일링을 검토한 후, @src/lib/prompts/generation.tsx의 생성 프롬프트를 업데이트해 앞으로 더 나은 컴포넌트를 생성하도록 해주세요."*

MCP 생태계에는 다음과 같은 서버들이 포함됩니다.

- 데이터베이스 상호작용
- API 테스트 및 모니터링
- 파일 시스템 작업
- 클라우드 서비스 통합
- 개발 도구 자동화

---

> **유형:** Video Lesson Claude Code는 GitHub Actions 내에서 Claude를 실행할 수 있는 공식 GitHub 연동 기능을 제공합니다. 이 연동은 두 가지 주요 워크플로우를 제공합니다. 이슈 및 풀 리퀘스트에서 멘션 지원과 자동 풀 리퀘스트 리뷰입니다.

#### 연동 설정하기

시작하려면 Claude에서 `/install-github-app` 을 실행하세요. 이 명령은 설정 과정을 안내합니다.

1. GitHub에 Claude Code 앱 설치
2. API 키 추가
3. 워크플로우 파일이 포함된 풀 리퀘스트 자동 생성

병합 후 `.github/workflows` 디렉토리에 워크플로우 파일이 생성됩니다.

**멘션 액션(Mention Action)** 이슈나 풀 리퀘스트에서 `@claude` 를 사용해 Claude를 멘션할 수 있습니다. 멘션되면 Claude는 다음을 수행합니다.

- 요청을 분석하고 작업 계획 수립
- 전체 코드베이스에 접근해 작업 실행
- 이슈나 PR에 직접 결과 응답

**풀 리퀘스트 액션(Pull Request Action)** 풀 리퀘스트를 생성할 때마다 Claude가 자동으로 다음을 수행합니다.

- 제안된 변경 사항 검토
- 수정 사항의 영향 분석
- 풀 리퀘스트에 상세 리포트 게시

#### 워크플로우 커스터마이징

초기 풀 리퀘스트를 병합한 후 프로젝트 요구에 맞게 워크플로우 파일을 커스터마이징할 수 있습니다.

**프로젝트 설정 추가**

```
- name: Project Setup

  run: |

    npm run setup

    npm run dev:daemon
```

**커스텀 지시사항**

```
custom_instructions: |

  The project is already set up with all dependencies installed.

  The server is already running at localhost:3000.

  Logs from it are being written to logs.txt.

  If needed, you can query the db with the 'sqlite3' cli.

  If needed, use the mcp__playwright set of tools to launch a browser and interact with the app.
```

**MCP 서버 구성**

```
mcp_config: |

  {

    "mcpServers": {

      "playwright": {

        "command": "npx",

        "args": [

          "@playwright/mcp@latest",

          "--allowed-origins",

          "localhost:3000;cdn.tailwindcss.com;esm.sh"

        ]

      }

    }

  }
```

**툴 권한** 로컬 개발과 달리 GitHub Actions에서는 권한에 대한 단축키가 없습니다. 각 MCP 서버의 각 툴을 개별적으로 나열해야 합니다.

```
allowed_tools: "Bash(npm:*),Bash(sqlite3:*),mcp__playwright__browser_snapshot,mcp__playwright__browser_click,..."
```

---

---

> **유형:** Video Lesson 훅(hook)을 사용하면 Claude가 툴을 실행하기 전후에 명령을 실행할 수 있습니다. 파일 편집 후 코드 포맷터 실행, 파일 변경 시 테스트 실행, 특정 파일에 대한 접근 차단 등 자동화된 워크플로우를 구현하는 데 매우 유용합니다.

Claude에게 질문을 하면 쿼리가 툴 정의와 함께 Claude 모델에 전송됩니다. Claude는 형식화된 응답을 제공해 툴을 사용하기로 결정할 수 있으며, 그러면 Claude Code가 해당 툴을 실행하고 결과를 반환합니다. 훅은 이 프로세스에 개입해 툴 실행 직전 또는 직후에 코드를 실행할 수 있게 합니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FsDtMkabnSS4wZPthq1GT%2F010_%2520_Introducing_Hooks_06.1752618158162.png&width=768&dpr=3&quality=100&sign=55518f7f&sv=2)

Hook flow overview

유형

실행 시점

차단 가능 여부

`PreToolUse`

✅ 가능

`PostToolUse`

❌ 불가

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F6vPJe7Dsi76ROxdLah5n%2F010_%2520_Introducing_Hooks_07.1752618158600.png&width=768&dpr=3&quality=100&sign=2e026e97&sv=2)

PreToolUse vs PostToolUse

#### 훅 구성

훅은 Claude 설정 파일에 정의합니다. 다음 위치에 추가할 수 있습니다.

위치

범위

`~/.claude/settings.json`

`.claude/settings.json`

`.claude/settings.local.json`

이 파일을 직접 편집하거나 Claude Code 내에서 `/hooks` 명령을 사용해 훅을 작성할 수 있습니다.

**PreToolUse 훅 예시:**

```
"PreToolUse": [

  {

    "matcher": "Read",

    "hooks": [

      {

        "type": "command",

        "command": "node /home/hooks/read_hook.ts"

      }

    ]

  }

]
```

**PostToolUse 훅 예시:**

```
"PostToolUse": [

  {

    "matcher": "Write|Edit|MultiEdit",

    "hooks": [

      {

        "type": "command",

        "command": "node /home/hooks/edit_hook.ts"

      }

    ]

  }

]
```

- **코드 포맷팅** — Claude가 파일을 편집한 후 자동으로 포맷 적용
- **테스트** — 파일 변경 시 자동으로 테스트 실행
- **접근 제어** — 특정 파일을 읽거나 편집하는 것을 차단
- **코드 품질** — 린터 또는 타입 체커를 실행하고 Claude에 피드백 제공
- **로깅** — Claude가 접근하거나 수정하는 파일 추적
- **유효성 검사** — 네이밍 규칙 또는 코딩 표준 확인

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FYn50KzxMLeFdz72czTfz%2F010_%2520_Introducing_Hooks_10.1752618159645.png&width=768&dpr=3&quality=100&sign=a2f962fa&sv=2)

Hook practical example

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FFxmQhOeMh0J5GrY95EBi%2F010_%2520_Introducing_Hooks_15.1752618160073.png&width=768&dpr=3&quality=100&sign=6a04793d&sv=2)

Hook configuration in settings

---

> **유형:** Video Lesson Claude Code의 훅을 사용하면 툴 호출을 실행 전후에 가로채고 제어할 수 있습니다. 이를 통해 개발 환경에서 Claude가 할 수 있는 것과 할 수 없는 것을 세밀하게 제어할 수 있습니다.

1

PreToolUse 또는 PostToolUse 훅 **결정**

2

감시할 툴 호출 유형 **확인**

3

툴 호출을 수신할 명령 **작성** (stdin을 통해 JSON 수신)

4

종료 코드를 통해 Claude에 **피드백 반환**

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FhqaAiXzFOSdbaxbsariq%2F011_%2520_Defining_Hooks_05.1752618152864.png&width=768&dpr=3&quality=100&sign=3fe8d711&sv=2)

Hook building steps

훅 명령이 실행되면 Claude는 표준 입력(stdin)을 통해 JSON 데이터를 전송합니다.

```
{

  "session_id": "2d6a1e4d-6...",

  "transcript_path": "/Users/sg/...",

  "hook_event_name": "PreToolUse",

  "tool_name": "Read",

  "tool_input": {

    "file_path": "/code/queries/.env"

  }

}
```

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FjypsGJDLCBkVrwGyZIWF%2F011_%2520_Defining_Hooks_07.1752618153492.png&width=768&dpr=3&quality=100&sign=fd53840a&sv=2)

Tool call data structure

종료 코드

의미

`0`

`2`

종료 코드 2로 종료하면 **stderr** 에 작성된 오류 메시지가 작업이 차단된 이유를 설명하는 피드백으로 Claude에 전송됩니다.

> **보충 설명:**
> 
> - **stdout vs stderr 구분:**`stdout` (표준 출력)에 출력한 내용은 Claude에게 **참고 정보** 로 전달됩니다(차단하지 않음). `stderr` (표준 오류)에 출력한 내용은 exit code 2와 함께 **차단 이유** 로 Claude에게 전달됩니다. 즉, 차단 메시지는 반드시 `console.error()` 또는 `stderr` 에 작성해야 합니다.
> - **종료 코드 1과 2의 차이:** 종료 코드 `1` 은 훅 스크립트 자체의 오류(예: 문법 오류, 실행 실패)로 처리됩니다. 의도적으로 툴을 차단할 때는 반드시 `2` 를 사용하세요.
> - **훅 타임아웃:** 훅 실행은 기본적으로 **60초 타임아웃** 이 적용됩니다. 오래 걸리는 작업(예: 별도 Claude 인스턴스 실행)을 훅에서 수행할 경우 이 한도를 고려해야 합니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FXrGxDa2ShHCWon98Xxkt%2F011_%2520_Defining_Hooks_11.1752618154320.png&width=768&dpr=3&quality=100&sign=7677fde0&sv=2)

Exit code flow

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2FF5CY77rc9FqjSBT4ZPgx%2F011_%2520_Defining_Hooks_16.1752618154725.png&width=768&dpr=3&quality=100&sign=ddd5f226&sv=2)

Hook blocking example

---

> **유형:** Video Lesson Claude가 `.env` 와 같은 민감한 파일을 읽지 못하도록 방지하는 커스텀 훅을 만들어 봅시다.

`.claude/settings.local.json` 파일을 열고 PreToolUse 훅을 만드세요. 매처(matcher)는 read와 grep 작업을 모두 감지하도록 설정합니다.

```
"matcher": "Read|Grep"
```

파이프 기호(`|`)는 OR 연산자로 작동합니다. 명령은 다음과 같이 설정합니다.

```
"command": "node ./hooks/read_hook.js"
```

```
async function main() {

  const chunks = [];

  for await (const chunk of process.stdin) {

    chunks.push(chunk);

  }

  const toolArgs = JSON.parse(Buffer.concat(chunks).toString());

  // Extract the file path Claude is trying to read

  const readPath = toolArgs.tool_input?.file_path || toolArgs.tool_input?.path || "";

  // Check if Claude is trying to read the .env file

  if (readPath.includes('.env')) {

    console.error("You cannot read the .env file");

    process.exit(2);

  }

}
```

Claude가 읽기 작업을 시도하면 훅이 이를 가로채고 오류 메시지를 반환합니다. Claude는 작업이 차단되었음을 인식하고 이를 사용자에게 설명합니다.

#### 주요 이점

- **사전 예방적 보호** — 민감한 데이터를 읽기 전에 접근 차단
- **투명한 작동** — Claude가 작업 실패 이유를 이해
- **유연한 매칭** — 여러 툴(read, grep 등)과 함께 작동
- **명확한 피드백** — 의미 있는 오류 메시지 제공

---

> **유형:** Text Lesson `npm run dev` 명령을 실행한 후 `.claude` 디렉토리에 두 개의 `settings.json` 파일이 있는 것을 발견할 수 있습니다. 그 이유를 설명해 드리겠습니다.

Claude Code 문서에는 훅 보안과 관련한 몇 가지 권장 사항이 나와 있습니다. 그 중 하나는 스크립트에 상대 경로 대신 **절대 경로** 를 사용하라는 것입니다. 이는 [경로 가로채기(path interception)](https://attack.mitre.org/techniques/T1574/007/) 및 [바이너리 이식(binary planting)](https://owasp.org/www-community/attacks/Binary_planting) 위험을 완화하기 위함입니다.

이 권장 사항은 파일 공유를 훨씬 어렵게 만들기도 합니다. 이유는 간단합니다. **나의** 머신의 절대 경로는 다른 사람의 머신 경로와 다르기 때문입니다.

이 문제를 해결하기 위해 프로젝트에는 `settings.example.json` 파일이 있습니다. 이 파일에서 스크립트 참조에는 `$PWD` 라는 플레이스홀더가 포함되어 있습니다. `npm run setup` 을 실행하면 `init-claude.js` 스크립트가 `$PWD` 를 실제 작업 디렉토리로 교체하고, 결과를 `settings.local.json` 으로 저장합니다.

이 스크립트를 통해 `settings.json` 파일을 공유하면서도 권장 절대 경로를 사용할 수 있습니다!

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F72vD3emlu3fSra69QLz7%2FScreenshot%2B2025%252007%252016%2Bat%2B10.25.07%25E2%2580%25AFAM.1752683124012.png&width=768&dpr=3&quality=100&sign=712e896e&sv=2)

settings.example.json and settings.local.json

---

> **유형:** Video Lesson Claude Code 훅은 특히 대형 프로젝트에서 AI 보조 개발의 일반적인 약점을 보완하는 데 도움이 됩니다. 이 훅들은 Claude가 코드를 수정할 때 자동으로 실행되어 즉각적인 피드백을 제공하고 일반적인 문제를 예방합니다.

가장 유용한 훅 중 하나는 근본적인 문제를 해결합니다. Claude가 함수 시그니처를 수정할 때 프로젝트 전체에서 해당 함수가 호출되는 모든 위치를 업데이트하지 않는 경우가 많습니다.

예를 들어 `schema.ts` 의 함수에 `verbose` 파라미터를 추가해 달라고 하면, Claude는 함수 정의는 성공적으로 업데이트하지만 `main.ts` 의 호출 위치는 놓칠 수 있습니다. 이로 인해 Claude가 즉시 감지하지 못하는 타입 오류가 발생합니다.

해결책은 모든 파일 편집 후 TypeScript 컴파일러를 실행하는 **post-tool-use 훅** 입니다.

1. `tsc --noEmit` 을 실행해 타입 오류 확인
2. 발견된 오류 캡처
3. 즉시 Claude에 오류 피드백
4. Claude가 다른 파일의 문제를 수정하도록 유도

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F7aD5hRGUykAR1SjAlRMG%2F013_%2520_Useful_Hooks%21_09.1752618172075.png&width=768&dpr=3&quality=100&sign=1e25aa&sv=2)

TypeScript hook flow

많은 데이터베이스 쿼리가 있는 대형 프로젝트에서 Claude는 기존 코드를 재사용하는 대신 중복 기능을 만드는 경우가 있습니다. 여러 쿼리 파일이 있는 프로젝트 구조를 생각해 보세요. Claude에게 "3일 이상 보류 중인 주문에 대해 Slack 알림을 보내는 통합 기능을 만들어 달라"고 하면, 기존의 `getPendingOrders()` 함수를 사용하는 대신 새로운 쿼리를 작성할 수 있습니다.

쿼리 중복 방지 훅은 다음 검토 프로세스를 구현합니다.

1

Claude가 `./queries` 디렉토리의 파일을 수정할 때 트리거

2

프로그래밍 방식으로 별도의 Claude Code 인스턴스 실행

3

두 번째 인스턴스가 변경 사항을 검토하고 유사한 기존 쿼리 확인

4

중복이 발견되면 원래 Claude 인스턴스에 피드백 제공

5

Claude가 중복을 제거하고 기존 기능을 사용하도록 유도

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F35j3UE2Rekx7RgaAMxD6%2F013_%2520_Useful_Hooks%21_14.1752618172611.png&width=768&dpr=3&quality=100&sign=1d37695&sv=2)

Query duplication prevention hook

- TypeScript 훅은 비교적 가볍고 빠르게 실행됩니다.
- 쿼리 중복 방지 훅은 각 검토마다 별도의 Claude 인스턴스를 실행하므로 더 많은 리소스가 필요합니다.
- **권장 사항:** 오버헤드를 최소화하기 위해 핵심 디렉토리만 모니터링하세요.

---

> **유형:** Text Lesson 이 코스에서 다룬 `PreToolUse` 와 `PostToolUse` 훅 외에도 추가적인 훅이 있습니다.

훅

실행 시점

`Notification`

`Stop`

`SubagentStop`

`PreCompact`

`UserPromptSubmit`

`SessionStart`

`SessionEnd`

혼란스러울 수 있는 부분입니다.

- 명령에 대한 stdin 입력은 **실행되는 훅 유형** (`PreToolUse`, `PostToolUse`, `Notification` 등)에 따라 **달라집니다**.
- `PreToolUse` 와 `PostToolUse` 훅의 경우, 포함된 `tool_input` 은 **호출된 툴에 따라 달라집니다**.

`**TodoWrite**` **를 감시하는** `**PostToolUse**` **훅의 stdin 예시:**

```
{

  "session_id": "9ecf22fa-edf8-4332-ae85-b6d5456eda64",

  "transcript_path": "<path_to_transcript>",

  "hook_event_name": "PostToolUse",

  "tool_name": "TodoWrite",

  "tool_input": {

    "todos": [

      {

        "content": "write a readme",

        "status": "pending",

        "priority": "medium",

        "id": "1"

      }

    ]

  },

  "tool_response": {

    "oldTodos": [],

    "newTodos": [

      {

        "content": "write a readme",

        "status": "pending",

        "priority": "medium",

        "id": "1"

      }

    ]

  }

}
```

`**Stop**` **훅의 stdin 예시:**

```
{

  "session_id": "af9f50b6-f042-4773-b3e2-c3a4814765ce",

  "transcript_path": "<path_to_transcript>",

  "hook_event_name": "Stop",

  "stop_hook_active": false

}
```

다양한 입력 형식을 처리하기 위해 다음과 같은 헬퍼 훅을 만들어 보세요.

```
{

  "PostToolUse": [

    {

      "matcher": "*",

      "hooks": [

        {

          "type": "command",

          "command": "jq . > post-log.json"

        }

      ]

    }

  ]

}
```

이렇게 하면 입력이 `post-log.json` 파일에 기록되어 명령이 어떤 데이터를 검사해야 하는지 훨씬 쉽게 파악할 수 있습니다.

---

> **유형:** Video Lesson Claude Code SDK를 사용하면 자체 애플리케이션과 스크립트 내에서 Claude Code를 프로그래밍 방식으로 실행할 수 있습니다. TypeScript, Python 및 CLI를 통해 사용할 수 있습니다. SDK는 여러분이 이미 익숙한 Claude Code와 완전히 동일하게 실행됩니다. 동일한 모든 툴에 접근할 수 있으며, 주어진 작업을 완수하기 위해 툴을 활용합니다.

![](https://keunyoung.gitbook.io/claude-course/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2F45kwo0E64wphXqzBIgZ3%2Fblobs%2F0ocy0QLLi850cYOf6RK4%2F014_%2520_The_Claude_Code_SDK_00.1752618201045.png&width=768&dpr=3&quality=100&sign=2229bc3c&sv=2)

Claude Code SDK overview

#### 주요 기능

- Claude Code를 프로그래밍 방식으로 실행
- 터미널 버전과 동일한 Claude Code 기능 제공
- 동일한 디렉토리의 Claude Code 인스턴스에서 모든 설정 상속
- **기본적으로 읽기 전용 권한**
- 더 큰 파이프라인이나 도구의 일부로 활용할 때 가장 유용

```
import { query } from "@anthropic-ai/claude-code";

const prompt = "Look for duplicate queries in the ./src/queries dir";

for await (const message of query({ prompt })) {

  console.log(JSON.stringify(message, null, 2));

}
```

이 코드를 실행하면 로컬 Claude Code와 Claude 언어 모델 간의 원시 대화를 메시지 단위로 확인할 수 있습니다. 마지막 메시지에 Claude의 완전한 응답이 포함됩니다.

#### 권한과 툴

기본적으로 SDK는 읽기 전용 권한만 가집니다. 쓰기 권한을 활성화하려면 다음과 같이 하세요.

```
for await (const message of query({

  prompt,

  options: {

    allowedTools: ["Edit"]

  }

})) {

  console.log(JSON.stringify(message, null, 2));

}
```

또는 `.claude` 디렉토리 내의 설정 파일에서 권한을 구성해 프로젝트 전체에 접근 권한을 부여할 수 있습니다.

- 코드 변경 사항을 자동으로 검토하는 Git 훅
- 코드를 분석하고 최적화하는 빌드 스크립트
- 코드 유지보수 작업을 위한 헬퍼 명령어
- 자동화된 문서 생성
- CI/CD 파이프라인에서의 코드 품질 검사

---

출처: [Anthropic Academy — Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

Last updated