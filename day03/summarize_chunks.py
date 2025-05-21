import os
import openai
from dotenv import load_dotenv
import argparse
import textwrap

# 🔐 API 키 로딩
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 📦 블록 분할 함수
def split_text(text, chunk_size=1000):
    return textwrap.wrap(text, chunk_size)

# 🧠 GPT 요청 함수
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# 🚀 메인 로직
def main():
    parser = argparse.ArgumentParser(description="긴 텍스트 분할 요약기")
    parser.add_argument("input_file", help="요약할 긴 텍스트 파일 경로")
    parser.add_argument("--output", "-o", default="day03/final_summary.txt", help="출력 파일명")
    parser.add_argument("--chunk_size", "-c", type=int, default=1000, help="텍스트 분할 크기 (기본 1000자)")
    parser.add_argument("--limit", "-l", type=int, default=3, help="최종 요약 문장 수")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"❌ 파일이 존재하지 않습니다: {args.input_file}")
        return

    with open(args.input_file, "r", encoding="utf-8") as f:
        full_text = f.read()

    chunks = split_text(full_text, args.chunk_size)
    print(f"📚 총 {len(chunks)}개의 블록으로 분할됨")

    block_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"🧠 블록 {i+1}/{len(chunks)} 요약 중...")
        prompt = f"다음 텍스트를 요약해줘:\n\n{chunk}"
        summary = ask_gpt(prompt)
        block_summaries.append(summary)

    merged_summary = "\n\n".join(block_summaries)
    print("🧠 전체 요약 종합 중...")

    final_prompt = (
        f"다음 내용을 종합해서 {args.limit}문장 이내로 요약해줘. "
        "각 문장은 줄바꿈으로 구분해줘:\n\n" + merged_summary
    )
    final_summary = ask_gpt(final_prompt)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print(f"✅ 최종 요약 저장 완료: {args.output}")

if __name__ == "__main__":
    main()
