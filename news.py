



import requests
from bs4 import BeautifulSoup
url=requests.get("http://yandex.ru")

soup=BeautifulSoup(url.text, "html.parser")
news=soup.find_all(class_="news__item-content")

for current_news in news:
    print( current_news.text)
    