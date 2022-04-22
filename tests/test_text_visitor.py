from app.models.text_visitor import TextVisitor
from unittest.mock import patch, MagicMock
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

def test_visit_webpage(example_html):
    webpage_mock = MagicMock(name="Webpage Mock", **{"get_html.return_value": example_html})
    
    visitor = TextVisitor()
    webpage_text = visitor.visit_webpage(webpage_mock)

    assert "Some Div Text" in webpage_text
    assert "Some Body Text" in webpage_text
    assert "Some Head Text" in webpage_text
    assert "<head" not in webpage_text
    assert "<div" not in webpage_text

