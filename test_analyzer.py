import json
from src.website_reader import extract_website_content
from src.company_analyzer import analyze_company

url = "https://www.netflix.com"

print("Reading company website...")

website_data = extract_website_content(url)

print("Analyzing company with AI...")

company_data = analyze_company(
    website_data=website_data,
    provider="ollama"
)

print("\nSTRUCTURED COMPANY INTELLIGENCE")
print("=" * 50)

print(json.dumps(company_data, indent=4))

