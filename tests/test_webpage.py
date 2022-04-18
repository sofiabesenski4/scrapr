from app.models.webpage import Webpage
import pytest

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

def test_webpage(example_html):    

    page = Webpage(example_html)

    assert "Some Div Text" in page.text
    assert "Some Body Text" in page.text
    assert "Some Head Text" in page.text
    assert "<head" not in page.text
    assert "<div" not in page.text
