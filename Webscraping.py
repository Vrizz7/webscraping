from lxml import html
import requests
import pymysql

link = input('\n')
urlempik = link

titlepath = '//*[@id="layoutContent"]/div[1]/div[2]/div[2]/div[1]/h1/text()'
pricepath = '//*[@id="sellerNavBox-1"]/div/div/div[1]/div[2]/text()'

pageempik = requests.get(urlempik)

tree = html.fromstring(pageempik.text)

title = tree.xpath(titlepath)
price = tree.xpath(pricepath)

title = ''.join(title)
price = ''.join(price)

connect = pymysql.connect(host='localhost', user='root', password='', db='empik')
cur = connect.cursor()

try:
    id = 1
    cur.execute("INSERT INTO books (id, title, price) VALUES (%s, %s, %s)",
                (id, title, price))
    connect.commit()
except:
    print("fail")
