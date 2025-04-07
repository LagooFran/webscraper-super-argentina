import requests

def getMeli():
    url = "https://listado.mercadolibre.com.ar/mouse#D[A:mouse]"
    r = requests.get(url)
    return r.text
