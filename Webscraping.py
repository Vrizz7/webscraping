from lxml import html
import requests
import msvcrt

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

print ("Tytul: " + title + "\n Cena: " + price)

file = open ('C:\\Users\\Mistrz\\Desktop\\book.txt', 'w')

file.write("Tytuł: " + title + "\n Cena: " + price)

file.close()
