from tools import vtexRequestBuilder
from models.Product import Product
import requests


def GetProds(query, cant, baseUrl, debug):

    res = requests.get(vtexRequestBuilder.BuildRequest(query, cant, baseUrl, debug))
    products = {}


    #extraigo los valores importantes de cada producto una vez que recibo el json de la request, en algunos casos hay pequenias variaciones 
    #entre los formatos de cada pagina web
    #get all important values from every product requested, sometimes there are little variations between the diferent stores webpages
    
    for count, key in enumerate(res.json()["data"]["productSuggestions"]["products"]):

        name = key["productName"]
        price = key["priceRange"]["sellingPrice"]["highPrice"]
        brand = key["brand"]
        pricePUnit = ""
        imgUrl = key["items"][0]["images"][0]["imageUrl"]
        
        for value in key["properties"]:
            if(value["name"] == "Precio x unidad"):
                pricePUnit = value["values"][0]

        prod = Product(name, price, brand, pricePUnit, imgUrl)
        products.setdefault(count, prod.ToDict())

    return products