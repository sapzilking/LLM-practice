import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 대화 초기 메시지 설정
messages = [{"role": "system", "content": "당신은 친절한 AI 비서입니다."}]

print("💬 GPT 챗봇 시작! 종료하려면 'exit' 입력")

while True:
    user_input = input("👤 당신: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print("🤖 GPT:", reply)
