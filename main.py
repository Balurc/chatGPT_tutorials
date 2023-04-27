import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

while True:
  question = input("\033[34mSebutkan Pertanyaan Anda?\n\033[0m")

  if question.lower() == "selesai":
    print("\033[31mSampai Jumpa Lagi!\n\033[0m")
    break

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an assistant. Answer the given question."},
      {"role":"user", "content":question},
    ]
  )

  print("\033[32m" + completion.choices[0].message.content + "\n")


