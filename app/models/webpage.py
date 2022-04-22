import requests

class Webpage:
    def __init__(self, url):
        self.url = url 

    def accept(self, visitor):
        return  visitor.visit_webpage(self)        
    
    def get_html(self):
        r = requests.get(self.url)
        return r.text

