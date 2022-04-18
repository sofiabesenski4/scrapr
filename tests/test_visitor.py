from app.models.visitor import Visitor
from unittest.mock import patch, MagicMock

@patch("app.models.visitor.requests.get")
def test_get_html(requests_get_mock):
    requests_get_text_mock = MagicMock(name="get_text_mock")
    requests_get_text_mock.text="""
        <head>
            Some head
        </head>
        <body>
            Some Body Text
            <div>
                Some Div Text
            </div>
        </body>
    """
    requests_get_mock.return_value = requests_get_text_mock

    visitor = Visitor("http://www.placecage.com")
    html = visitor.get_html()

    assert "Some head" in html
    assert "<div" in html
    assert "<body" in html
    print(html)
