
from src.website_reader import extract_website_content


url = "https://apple.com"

website = extract_website_content(url)

print("\nWEBSITE TITLE:")
print(website["title"])

print("\nWEBSITE CONTENT:")
print(website["content"])
