import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "안녕 GPT야. 오늘 날씨 어때?"}
    ]
)

print(response['choices'][0]['message']['content'])
