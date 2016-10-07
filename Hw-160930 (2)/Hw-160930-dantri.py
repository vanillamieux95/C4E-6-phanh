from bs4 import *
import urllib.request

class HotNews:
    def __init__(self, title, link):
        self.title = title
        self.link = link

with urllib.request.urlopen('http://dantri.com.vn/') as response:
   html = response.read()
   soup = BeautifulSoup(html, 'html.parser')

   soup.find("div", "line1 mt1")
