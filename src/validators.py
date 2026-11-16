
from urllib.parse import urlparse


def validate_website_url(url):

    if not url or not url.strip():
        raise ValueError("Website URL cannot be empty.")

    url = url.strip()

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ["http", "https"]:
        raise ValueError("URL must start with http:// or https://")

    if not parsed_url.netloc:
        raise ValueError("Please enter a valid website URL.")

    if "." not in parsed_url.netloc:
        raise ValueError("Please enter a valid domain name.")

    if parsed_url.username or parsed_url.password:
        raise ValueError("URLs containing credentials are not allowed.")

    return url
