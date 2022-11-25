from bs4 import BeautifulSoup
from array import *
import requests

def paladiy():
    url = 'https://investfunds.ru/indexes/400/'
    site = requests.get(url)
    information = BeautifulSoup(site.text, 'lxml')
    information = information.find_all('div', class_="js_td_width")
    a = []
    b = ""
    i = 0
    for point in information:
        if (i < 10):
            a.append(point.text)
            b = b + f'{i}' + " дней назад: " + point.text + ' рублей | \n'
        i = i + 1
    print(b)
    return b

paladiy()
