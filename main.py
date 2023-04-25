import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

question = input("\033[31mWhat is your question?\n\033[0m")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an assistant. Answer the given question."},
    {"role":"user", "content":question},
  ]
)

print(question)

# print(completion.choices[0].message)


