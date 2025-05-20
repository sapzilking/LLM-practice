import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

# 저장 함수
def save_chat_log(messages, filename="chat_log.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for msg in messages:
            role = msg["role"].upper()
            if role == "SYSTEM":
                continue  # 프롬프트 지시는 생략
            content = msg["content"]
            f.write(f"{role}: {content}\n\n")


roles = {
    "1": "당신은 텍스트를 간결하게 요약해주는 요약기입니다.",
    "2": "당신은 문장을 자연스러운 영어로 고쳐주는 영어 튜터입니다.",
    "3": "당신은 한국어 문장을 영어로 번역해주는 번역기입니다."
}

print("🤖 사용할 GPT 역할을 선택하세요:")
print("1. 요약기 | 2. 영어 튜터 | 3. 번역기")
choice = input("번호 입력 (기본=1): ").strip()

# 유효성 체크 & 기본값 처리
role_content = roles.get(choice, roles["1"])
messages = [{"role": "system", "content": role_content}]



# 대화 초기 메시지 설정
# messages = [{"role": "system", "content": "당신은 친절한 AI 비서입니다."}]

print("💬 GPT 챗봇 시작! 종료하려면 'exit' 입력")

while True:
    user_input = input("👤 당신: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 종료합니다.")
        break
    if user_input.lower() == "/save":
        save_chat_log(messages)
        print("💾 대화가 chat_log.txt에 저장되었습니다.")
        continue

    messages.append({"role": "user", "content": user_input})
    reply=ask_gpt(messages)
    print("🤖 GPT:", reply)
