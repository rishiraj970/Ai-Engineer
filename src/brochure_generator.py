
from src.llm_client import generate_response, generate_response_stream


def build_brochure_prompt(company_data):

    return f"""
You are an expert marketing copywriter.

Create a professional sales brochure using the company
information provided below.

COMPANY INFORMATION:
{company_data}

BROCHURE REQUIREMENTS:

1. Write an engaging headline.
2. Introduce the company.
3. Highlight its main products and services.
4. Explain who its target customers are.
5. Highlight its competitive advantages.
6. End with a compelling call to action.

IMPORTANT:
- Use only the information provided.
- Do not invent statistics, awards, certifications or claims.
- Do not invent contact details.
- Keep the language professional and persuasive.
- Use clear headings and bullet points.
- Format the brochure using Markdown.
"""


def generate_brochure(company_data, provider="ollama"):

    prompt = build_brochure_prompt(company_data)

    return generate_response(
        prompt=prompt,
        provider=provider
    )


def generate_brochure_stream(company_data, provider="ollama"):

    prompt = build_brochure_prompt(company_data)

    for chunk in generate_response_stream(
        prompt=prompt,
        provider=provider
    ):
        yield chunk
