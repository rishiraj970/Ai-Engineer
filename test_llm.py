
from src.llm_client import generate_response

# Select our LLM provider
provider = "ollama"

prompt = """
Explain three ways AI can help businesses
improve customer experience.
"""

answer = generate_response(
    prompt=prompt,
    provider=provider
)

print("\nAI RESPONSE:\n")
print(answer)
