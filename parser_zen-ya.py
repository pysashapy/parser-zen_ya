#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req


def pars_url(url, w):
    print(url)
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    news = soup.findAll('a', class_='channel-item__link')

    for i in news:
        for j in range(len(i.text)):
            try:
                w.write((i.text)[j])
            except Exception as e:
                pass
        w.write(" - "+"https://zen.yandex.ru/"+i["href"]+"\n")
        print(i.text,"https://zen.yandex.ru/"+i["href"])
    url = soup.findAll('a', class_='pagination-prev-next__link')
    if url[-1]["href"] is not None and (len(url)==2 or url[0].text=="Следующие 20"):

        url2="https://zen.yandex.ru"+url[-1]["href"]
        w2 = open("url.txt","a", encoding='utf-8')
        pars_url(url2,w2)
    else: return "Сколько смог "

url = "https://zen.yandex.ru/media/zen/channels?page=13853"
a = open("url.txt","w", encoding='utf-8')
pars_url(url,a)
