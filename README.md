# LLM Practice

LLM(대형 언어 모델)을 활용한 애플리케이션 개발 실습 리포지토리입니다.  
이 프로젝트는 Python과 OpenAI GPT API를 중심으로 실습하며, 실전 중심의 LLM 활용 능력을 기르는 것을 목표로 합니다.

---

## 📅 Day 1: Python 기초 + GPT 챗봇

### 🔧 학습 내용

- Python 개발환경 세팅 (macOS, venv)
- 기본 문법 실습
  - 조건문, 반복문, 함수, 리스트/딕셔너리
- OpenAI GPT-3.5 API 사용해보기
- 간단한 챗봇 코드 작성 및 실행

### 🧪 주요 실습 코드

- `day01/basics.py`  
  → Python 문법 실습

- `day01/gpt_chatbot.py`  
  → OpenAI API를 이용한 GPT 챗봇 예제

### 🔐 보안 주의사항
- API 키는 `.env` 또는 로컬 파일로 관리하고, 깃허브에 업로드하지 않습니다
- `venv/`, 키 파일은 `.gitignore`로 제외

---

## ✅ 실행 방법

1. Python 3.10+ 설치
2. 가상환경 생성
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install openai python-dotenv
3. .env 파일 생성 (예: OPENAI_API_KEY=xxxx)
4. gpt_chatbot.py 실행
   ```bash
   python day01/gpt_chatbot.py

## Day 2: 대화형 GPT 챗봇 CLI

### 주요 기능

- 역할 선택 기능 (요약기, 영어 튜터, 번역기)
- 명령어 기반 제어 (/save, /role, /help)
- 대화 로그 저장 기능
- .env 파일로 API 키 분리

### 실행 방법

1. 가상환경 활성화
2. `.env` 파일 생성 후 API 키 입력
3. 실행
```bash
python3 day02/interactive_chatbot.py

