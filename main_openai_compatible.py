
from openai import OpenAI

# Connect the OpenAI client to our local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "system",
            "content": "You are a professional business analyst."
        },
        {
            "role": "user",
            "content": "Explain how AI can help a company increase sales."
        }
    ]
)

print(response.choices[0].message.content)
