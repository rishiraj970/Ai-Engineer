
import os
from openai import OpenAI


def get_llm_client(provider="ollama"):

    if provider == "ollama":

        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

        model = "qwen2.5:3b"

    elif provider == "openai":

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is not configured")

        client = OpenAI(api_key=api_key)

        model = "gpt-4.1-mini"

    else:
        raise ValueError("Unsupported LLM provider")

    return client, model


def generate_response(prompt, provider="ollama"):

    client, model = get_llm_client(provider)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a professional business analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_response_stream(prompt, provider="ollama"):

    client, model = get_llm_client(provider)

    stream = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a professional business analyst and marketing copywriter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            yield content

