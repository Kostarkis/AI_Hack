from openai import OpenAI
import os


def gptRequest(user, system, model='gpt-4', temperature=0.7):
    client = OpenAI(
        api_key="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"
    )
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user
            },
            {
                "role": "system",
                "content": system
            }
        ],
        model=model,
    )

    return response.choices[0].message.content
