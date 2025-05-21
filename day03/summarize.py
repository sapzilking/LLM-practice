import os
import openai
from dotenv import load_dotenv
import argparse

# 🔐 API 키 로딩
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🧠 GPT 요청 함수
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 🚀 main 함수
def main():
    parser = argparse.ArgumentParser(description="텍스트 요약기")
    parser.add_argument("input_file", help="요약할 텍스트 파일 경로")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    prompt = f"다음 텍스트를 간결하게 요약해줘:\n\n{text}"
    summary = ask_gpt(prompt)

    with open("day03/summary_output.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("✅ 요약 완료: summary_output.txt에 저장됨")

if __name__ == "__main__":
    main()
