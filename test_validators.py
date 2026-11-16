
import pytest

from src.validators import validate_website_url


def test_valid_https_url():

    result = validate_website_url(
        "https://www.apple.com"
    )

    assert result == "https://www.apple.com"


def test_valid_http_url():

    result = validate_website_url(
        "http://example.com"
    )

    assert result == "http://example.com"


def test_empty_url():

    with pytest.raises(ValueError):
        validate_website_url("")


def test_invalid_domain():

    with pytest.raises(ValueError):
        validate_website_url("hello123")


def test_ftp_url():

    with pytest.raises(ValueError):
        validate_website_url("ftp://example.com")
