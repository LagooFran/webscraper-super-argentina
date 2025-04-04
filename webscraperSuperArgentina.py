from scrapers import vtexScrapers

def getAllProductsWithQuery(query, cant, debug=True):

    finalRes = {}

    finalRes.setdefault("carrefour",vtexScrapers.GetCarrefour(query, cant, debug))

    finalRes.setdefault("jumbo", vtexScrapers.GetJumbo(query, cant, debug))

    finalRes.setdefault("dia",vtexScrapers.GetDia(query, cant, debug))

    finalRes.setdefault("disco", vtexScrapers.GetDisco(query, cant, debug))

    finalRes.setdefault("vea", vtexScrapers.GetVea(query, cant, debug))

    finalRes.setdefault("mas", vtexScrapers.GetMas(query, cant, debug))

    return finalRes



finalRes = getAllProductsWithQuery("coca cola", 4)

for store in finalRes:
    print(store)
    for prod in finalRes[store]:
        print(finalRes[store][prod])