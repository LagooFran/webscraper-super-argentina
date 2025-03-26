from tools import vtexRequestBuilder
import requests

res = requests.get(vtexRequestBuilder.BuildRequest("arroz", "https://www.carrefour.com.ar"))

for key in res.json()["data"]["productSuggestions"]["products"]:
    print(key["productName"])
