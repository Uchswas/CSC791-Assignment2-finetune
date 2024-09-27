import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.fine_tuning.jobs.create(
  training_file="file-BrQsJ9viZrqpVdnd54Kbu8Hl", 
  model="gpt-4o-mini-2024-07-18"
)

