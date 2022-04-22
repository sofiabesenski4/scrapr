from bs4 import BeautifulSoup

class TextVisitor:
    def visit_webpage(self, webpage):
        html = webpage.get_html()
        return self._get_text(html)

    def _get_text(self, raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        return soup.get_text()

