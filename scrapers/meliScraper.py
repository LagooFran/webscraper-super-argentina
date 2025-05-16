import requests
from bs4 import BeautifulSoup

def getMeli():
    url = "https://listado.mercadolibre.com.ar/mouse#D[A:mouse]"
    r = requests.get(url)
    return r.text
