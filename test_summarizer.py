
from src.website_reader import extract_website_content
from src.company_summarizer import summarize_company

#useless now
url = "https://www.netflix.com"

print("Reading company website...")

website_data = extract_website_content(url)

print("Website extracted successfully!")

print("\nGenerating company intelligence...\n")

summary = summarize_company(
    website_data=website_data,
    provider="ollama"
)

print("=" * 50)
print("AI GENERATED COMPANY SUMMARY")
print("=" * 50)

print(summary)
