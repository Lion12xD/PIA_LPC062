# Leonardo Hasiel Alvarado Zamora -1949295
# Importar modulos
import requests
import csv
from bs4 import BeautifulSoup
# Direccion de la pagina web
url = "http://quotes.toscrape.com/"
# Ejecutar GET-Request
response = requests.get(url)
# Analizar sintacticamente el archivo HTML de DS del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
authors = list()
for author in authors_html:
    authors.append(author.text)
for t in zip(quotes, authors):
    print(t)
with open('./zitate.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))
