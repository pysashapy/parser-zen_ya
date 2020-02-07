#!/usr/bin/python3
#coding: UTF-8

from bs4 import BeautifulSoup
import requests as req
import xlsxwriter
from threading import Thread


def pars_url(url, sheet,z,workbook):
    print(url)
    z2=z
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    news = soup.findAll('a', class_='channel-item__link')

    for i in news:
        print(i.text,"https://zen.yandex.ru"+i["href"])

        sheet.write(z2, 0, i.text)
        sheet.write(z2,1,"https://zen.yandex.ru"+i["href"])

        z2+=1

    url = soup.findAll('a', class_='pagination-prev-next__link')

    if url[-1]["href"] is not None and (len(url)==2 or url[0].text=="Следующие 20"):
        if z%975==0:
            workbook.close()
            exit()
        url2="https://zen.yandex.ru"+url[-1]["href"]
        try:
            workbook2=workbook
            pars_url(url2,sheet,z2,workbook2)

        finally:
            workbook.close()
    else: return "Сколько смог "

def main():
    url = "https://zen.yandex.ru/media/zen/channels?page=%s"
    __LIST__ = []
    try:
        print("!")
        a = int(input("Стр:"))
        for i,z in zip(range(13069,14000,975),range(1*a,20)):
            print("2!")
            workbook  = xlsxwriter.Workbook('filename%s.xlsx'%(z+2))
            worksheet = workbook.add_worksheet()
            pars_url(url%i,worksheet,1,workbook)

    except Exception as e:
        pass

if __name__ == '__main__':

    main()
