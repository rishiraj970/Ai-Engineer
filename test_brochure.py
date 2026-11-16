
import json

from src.website_reader import extract_website_content
from src.company_analyzer import analyze_company
from src.brochure_generator import generate_brochure


url = "https://www.netflix.com"

print("STEP 1: Reading company website...")

website_data = extract_website_content(url)

print("STEP 2: Analyzing company...")

company_data = analyze_company(
    website_data=website_data,
    provider="ollama"
)

print("STEP 3: Generating brochure...")

brochure = generate_brochure(
    company_data=company_data,
    provider="ollama"
)

print("\n" + "=" * 100)
print("AI GENERATED COMPANY BROCHURE")
print("=" * 100)

print(brochure)

# Save brochure as a Markdown file
with open("company_brochure.md", "w", encoding="utf-8") as file:
    file.write(brochure)

# Save company intelligence as JSON
with open("company_data.json", "w", encoding="utf-8") as file:
    json.dump(company_data, file, indent=4, ensure_ascii=False)

print("\nBrochure and company data saved successfully!")
