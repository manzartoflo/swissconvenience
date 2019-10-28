# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:50:17 2019

@author: Shaikh Manzar
"""
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

url = "https://www.swissconvenience.ch/mitglieder.html"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

table = soup.findAll('table', {'width': '80%'})
a = table[0].findAll('a')
links = []
for link in a:
    links.append(urljoin(url, link.attrs['href']))


file = open('assignmnt.csv', 'w')
header = "Name, Telephone, Fax, Email, Website\n"
file.write(header)

for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    name = soup.findAll('h1', {'class': 'first'})[0].text
    table = soup.findAll('table', {'width': '100%'})
    tab = table[0].findAll('table', {'width': '100%'})
    td = tab[1].findAll('td')
    tel = td[0].text.split("Telefon:")[1]
    fax = td[1].text.split("Fax:")[1]
    email = td[2].text.split("E-Mail:")[1].replace("(at)", '@')
    web = td[3].text.split('Website:')[1]
    print(name, tel, fax, email, web)
    file.write(name.replace(',', '') + ", " + tel + ", " + fax + ", " + email + ", " + web + "\n")
file.close()