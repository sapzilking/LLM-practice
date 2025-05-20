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

# 대화 초기 메시지 설정
messages = [{"role": "system", "content": "당신은 친절한 AI 비서입니다."}]

print("💬 GPT 챗봇 시작! 종료하려면 'exit' 입력")

while True:
    user_input = input("👤 당신: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})
    reply=ask_gpt(messages)
    print("🤖 GPT:", reply)
