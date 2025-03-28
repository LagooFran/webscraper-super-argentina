from scrapers import carrefour

res = carrefour.getProds("coca cola", 4)
for prod in res:
    print(res[prod])