from scrapers import vtexScrapers

#solo para testeos
#only for testing

res = vtexScrapers.GetCarrefour("coca cola", 4, True)
print("CARREFOUR----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetJumbo("coca cola", 4, True)
print("JUMBO-----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetDia("coca cola", 4, True)
print("DIA-----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetDisco("coca cola", 4, True)
print("DISCO-----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetVea("coca cola", 4, True)
print("VEA-----------------------")
for prod in res:
    print(res[prod])
res = vtexScrapers.GetMas("coca cola", 4, True)
print("MAS-----------------------")
for prod in res:
    print(res[prod])
