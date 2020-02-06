#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req
import xlsxwriter


def pars_url(url, sheet,z):
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

        url2="https://zen.yandex.ru"+url[-1]["href"]

        pars_url(url2,sheet,z2)
    else: return "Сколько смог "

def main():
    url = "https://zen.yandex.ru/media/zen/channels?page=1"

    workbook  = xlsxwriter.Workbook('filename.xlsx')
    worksheet = workbook.add_worksheet()

    try:
        pars_url(url,worksheet,1)

    finally:
        workbook.close()
if __name__ == '__main__':

    main()
