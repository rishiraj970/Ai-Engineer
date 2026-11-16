
import requests
from bs4 import BeautifulSoup

from src.validators import validate_website_url


def extract_website_content(url):

    url = validate_website_url(url)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

    except requests.exceptions.Timeout:
        raise RuntimeError("Website request timed out.")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Could not connect to the website.")

    except requests.exceptions.HTTPError as error:
        raise RuntimeError(
            f"Website returned an HTTP error: {error}"
        )

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "noscript"
    ]):
        element.decompose()

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "No title"
    )

    text = soup.get_text(separator=" ", strip=True)

    if not text:
        raise RuntimeError("No readable content found on website.")

    text = text[:15000]

    return {
        "title": title,
        "content": text
    }
