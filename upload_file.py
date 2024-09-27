import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.files.create(
  file=open("readme_fine_tuning_openapi.jsonl", "rb"),
  purpose="fine-tune"
)

print(response)
