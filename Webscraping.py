from lxml import html
import requests

#adres strony
urlempik = 'http://www.empik.com/wedrowiec-um2033-cormudian-suren,p1181453207,ksiazka-p'

#sciezka do elementu XPATH
titlepath = '//*[@id="layoutContent"]/div[1]/div[2]/div[2]/div[1]/h1/text()'
pricepath = '//*[@id="sellerNavBox-0"]/div/div/div[1]/div[2]/text()'

#pobranie strony
pageempik = requests.get(urlempik)

#parsowanie strony
tree = html.fromstring(pageempik.text)

#wyszukanie elementu
title = tree.xpath(titlepath)
price = tree.xpath(pricepath)

#usuwanie zbednych znakow
title = ''.join(title)
price = ''.join(price)

print ("Tytul: " + title + "\n Cena: " + price)

#otwarcie pliku
file = open ('C:\\Users\\Mistrz\\Desktop\\book.txt', 'w')

#zapis do pliku
file.write("Tytuł: " + title + "\n Cena: " + price)

#zamkniecie pliku
file.close()