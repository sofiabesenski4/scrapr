from app.models.webpage import Webpage
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def example_html():
    return """
    <head>
        Some Head Text
    </head>
    <body>
        Some Body Text
        <div>
            Some Div Text
        </div>
    </body>
    """

def test_accept(example_html):    
    visitor = MagicMock(name="Some Visitor", **{"visit_webpage.return_value": "some response"})
    
    page = Webpage("www.some-url.com")
    response = page.accept(visitor)

    assert response == "some response"

@patch("app.models.webpage.requests.get")
def test_get_html(requests_get_mock, example_html):
    requests_get_text_mock = MagicMock(name="get_text_mock")
    requests_get_text_mock.text= example_html
    requests_get_mock.return_value = requests_get_text_mock

    page = Webpage("www.some-url.com")

    webpage_html = page.get_html()

    assert "Some Div Text" in webpage_html
    assert "Some Body Text" in webpage_html
    assert "Some Head Text" in webpage_html
    assert "<head" in webpage_html
    assert "<div" in webpage_html
