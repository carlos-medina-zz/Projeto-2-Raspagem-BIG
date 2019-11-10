import requests
from bs4 import BeautifulSoup

page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

teste = soup.select("td b")

for item in teste:
    print (item, "\n")


'''
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('p')[0].get_text())
'''