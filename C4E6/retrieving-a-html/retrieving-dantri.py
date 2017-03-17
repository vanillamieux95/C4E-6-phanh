from bs4 import *
import urllib.request

class HotNews:
    def __init__(self, title, link):
        self.title = title
        self.link = link

with urllib.request.urlopen('https://www.fiverr.com/') as response:
   html = response.read()
   print(html)

   soup = BeautifulSoup(html, 'html.parser')
   # print(soup.prettify())

   print(soup.title)
   print(soup.title.string) #accessing value
   print(soup.title.name)

   #ul = soup.find("ul", "ul1 ulnew") #the closest tag that match

   #print(ul[class]) #accessing attribute
   #
   # li_list = ul.find_all("li")
   #
   # hot_news_list = []
   #
   # for li in li_list:
   #     a = li.h4.a
   #
   #     hot_news = HotNews(a["title"],
   #                        "http://dantri.com.vn" + a["href"]
   #                        )
   #     hot_news_list.append(hot_news)
   #
   #     print(a["title"])
   #     print("http://dantri.com.vn" + a["href"])
   #     print(".....................................................")
   # print(hot_news_list)
   #
   f=open("fiverr.html", "wb") # w = write, b= binary
   f.write(html)
   f.close()