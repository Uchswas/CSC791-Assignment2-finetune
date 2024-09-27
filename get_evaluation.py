import openai
import time
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

fine_tuning_job_id = 'ftjob-Ro6SYMsMP0GROi7zPyvrSMFJ'

def get_job_status(fine_tuning_job_id):
    job_status = openai.fine_tuning.jobs.retrieve(fine_tuning_job_id)
    return job_status.status

def get_checkpoints(fine_tuning_job_id):
    return openai.fine_tuning.jobs.list_events(fine_tuning_job_id=fine_tuning_job_id)

while True:
    job_status = get_job_status(fine_tuning_job_id)
    if job_status == 'succeeded':
        break
    elif job_status == 'failed':
        print("Fine-tuning job failed.")
        break
    time.sleep(2)

checkpoints = get_checkpoints(fine_tuning_job_id)


if checkpoints:
    for checkpoint in checkpoints:
        if checkpoint.data and ( checkpoint.data["step"] % 5 == 0):
            print(f"Checkpoint ID: {checkpoint.id}")
            print(f"Checkpoint Message: {checkpoint.message}")
            print(f"Created At: {checkpoint.created_at}")
            print(f"Step Number: {checkpoint.message.split()[-1]}")
            print(f"Data: {checkpoint.data}")
            print("="*50)
else:
    print("No checkpoint events found.")
