import requests

class Visitor:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        r = requests.get(self.url)
        return r.text
