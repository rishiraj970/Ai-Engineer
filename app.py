
import os
import gradio as gr
from src.validators import validate_website_url

from src.website_reader import extract_website_content
from src.company_analyzer import analyze_company
from src.brochure_generator import generate_brochure_stream


def create_brochure(url, provider):

    if not url.strip():
        yield "Please enter a company website URL.", None
        return

    try:
        yield "Reading company website...", None

        url = validate_website_url(url)

        website_data = extract_website_content(url)

        yield "Analyzing company information...", None

        company_data = analyze_company(
            website_data=website_data,
            provider=provider
        )

        yield "Generating brochure...", None

        brochure = ""

        for chunk in generate_brochure_stream(
            company_data=company_data,
            provider=provider
        ):
            brochure += chunk

            # Display the growing brochure
            yield brochure, None

        # Create output directory
        os.makedirs("outputs", exist_ok=True)

        # Save brochure
        file_path = os.path.join(
            "outputs",
            "company_brochure.md"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(brochure)

        yield brochure, file_path

    except Exception as error:
        yield f"Something went wrong: {error}", None


with gr.Blocks(
    title="AI Company Brochure Generator"
) as demo:

    gr.Markdown(
        """
        # AI Company Intelligence & Brochure Generator

        Enter a company's website URL to generate
        an AI-powered sales brochure.
        """
    )

    url_input = gr.Textbox(
        label="Company Website URL",
        placeholder="https://www.apple.com"
    )

    provider_input = gr.Dropdown(
        choices=["ollama", "openai"],
        value="ollama",
        label="Choose AI Provider"
    )

    generate_button = gr.Button(
        "Generate Brochure",
        variant="primary"
    )

    brochure_output = gr.Markdown(
        label="Generated Brochure"
    )

    download_output = gr.File(
        label="Download Your Brochure"
    )

    generate_button.click(
        fn=create_brochure,
        inputs=[url_input, provider_input],
        outputs=[brochure_output, download_output]
    )


demo.launch()
