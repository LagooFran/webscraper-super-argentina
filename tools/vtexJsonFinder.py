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
        unit = ""
        imgUrl = key["items"][0]["images"][0]["imageUrl"]
        
        #tuve que hacer muchas cosas para evitar que la lectura de properties se alargue mas de lo necesario
        #se deberia poder optimizar....

        flagOther = False
        for value in key["properties"]:
            if(value["name"] == "Precio x unidad"):
                pricePUnit = value["values"][0]
                if flagOther == True: break
                flagOther = True
            elif(value["name"] == "Gramaje factor de conversión"):
                pricePUnit = float(price)/float(value["values"][0])
                if flagOther == True: break
                flagOther = True
            elif(value["name"] == "Gramaje de unidad de medida"):
                unit = value["values"][0]
                if flagOther == True: break
                flagOther = True

        productUrl = baseUrl + str(key["link"]).replace("https://portal.vtexcommercestable.com.br", "")

        prod = Product(name, price, brand, pricePUnit, unit, imgUrl, productUrl)
        products.setdefault(count, prod.ToDict())

    return products