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
    parser.add_argument("--output", "-o", default="day03/summary_output.txt", help="출력 파일명 (기본값: day03/summary_output.txt)")
    parser.add_argument("--limit", "-l", type=int, default=3, help="요약 문장 수 제한 (기본: 3문장)")
    args = parser.parse_args()

    # 파일 존재 확인
    if not os.path.exists(args.input_file):
        print(f"❌ 파일이 존재하지 않습니다: {args.input_file}")
        return

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    prompt = f"다음 텍스트를 {args.limit}문장 이내로 요약해줘. 각 문장은 줄바꿈으로 구분해서 출력해줘:\n\n{text}"
    summary = ask_gpt(prompt)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"✅ 요약 완료: {args.output}에 저장됨")

if __name__ == "__main__":
    main()
