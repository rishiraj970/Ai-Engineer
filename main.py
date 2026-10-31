
import ollama

# Select the model we downloaded
MODEL = "qwen2.5:3b"

# Send a prompt to the model
response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a professional business analyst."
        },
        {
            "role": "user",
            "content": "Explain what Apple does in five bullet points."
        }
    ]
)

# Display the model's response
print(response.message.content)
