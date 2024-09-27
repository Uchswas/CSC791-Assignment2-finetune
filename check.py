import openai
import os
from dotenv import load_dotenv
load_dotenv()

from readme_data import READMEDATA
from constant import SYSTEM_TEXT

openai.api_key = os.getenv('OPENAI_API_KEY')


completion = openai.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::ABu9wIgW",
  messages=[
    {"role": "system", "content": SYSTEM_TEXT},
    {"role": "user", "content": READMEDATA}
  ]
)
print(completion.choices[0].message.content)