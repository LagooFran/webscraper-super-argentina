from tools import vtexRequestBuilder
from models.Product import Product
import requests


def getProds(query, cant):

    res = requests.get(vtexRequestBuilder.BuildRequest(query, cant, "https://www.carrefour.com.ar"))
    products = {}

    
    for count, key in enumerate(res.json()["data"]["productSuggestions"]["products"]):

        name = key["productName"]
        price = key["priceRange"]["sellingPrice"]["highPrice"]
        brand = key["brand"]
        
        for value in key["properties"]:
            if(value["name"] == "Precio x unidad"):
                pricePUnit = value["values"][0]

        prod = Product(name, price, brand, pricePUnit)
        products.setdefault(count, prod.ToDict())

    return products