from openai import OpenAI

client = OpenAI()

client.files.create(
    file=open("mydata.jsonl", "rb"),
    purpose="fine-tune"
)

client.fine_tuning.jobs.create(
    training_file="file-abc123",
    model="gpt-3.5-turbo"
)
