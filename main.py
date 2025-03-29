from scrapers import vtexScrapers

#solo para testeos
#only for testing

res = vtexScrapers.GetCarrefour("coca cola", 4, True)
print("Carrefour----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetJumbo("coca cola", 4, True)
print("JUMBO-----------------------")
for prod in res:
    print(res[prod])