import requests

class Visitor:
    def get_html(self, url):
        r = requests.get(url)
        return r.text
