import requests
from bs4 import BeautifulSoup
from summa import summarizer
import re

# Obtener el contenido HTML de la página web
enlace = input('Ingrese búsqueda:\n ')
#enlace = "https://es.wikipedia.org/wiki/Per%C3%BA"

response = requests.get(enlace)
html = response.text

# Utilizar BeautifulSoup para extraer el texto del artículo
soup = BeautifulSoup(html, 'html.parser')

# Obtener el elemento div con la clase mw-body-content
body_content = soup.find("div", class_="mw-body-content")

# Eliminar las tablas dentro del body content
for table in body_content.find_all('table'):
    table.decompose()

listaref_div = soup.find("div", class_="listaref")
if listaref_div:
    listaref_div.decompose()

# Obtener el texto del elemento body content actualizado
article_text = body_content.get_text()

# Remover [] y espacios extras
article_text = re.sub(r'\[[0-9]*\]',' ',article_text)
article_text = re.sub(r'\s+',' ',article_text)

# Generar el resumen utilizando el módulo 'summa'
summary = summarizer.summarize(article_text)

# Imprimir el resumen
print(summary)