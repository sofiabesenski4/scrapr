from bs4 import BeautifulSoup

class Webpage:
    def __init__(self, html_doc):
        self.html_doc = html_doc
        self.text = self._get_text(html_doc)

    def _get_text(self, raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        return soup.get_text()
