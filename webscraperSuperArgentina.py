from scrapers import vtexScrapers
from scrapers import meliScraper

def getAllVtexSiteProductsWithQuery(query, cant, debug=True):

    finalRes = {}

    finalRes.setdefault("carrefour",vtexScrapers.GetCarrefour(query, cant, debug))

    finalRes.setdefault("jumbo", vtexScrapers.GetJumbo(query, cant, debug))

    finalRes.setdefault("dia",vtexScrapers.GetDia(query, cant, debug))

    finalRes.setdefault("disco", vtexScrapers.GetDisco(query, cant, debug))

    finalRes.setdefault("vea", vtexScrapers.GetVea(query, cant, debug))

    finalRes.setdefault("mas", vtexScrapers.GetMas(query, cant, debug))

    return finalRes

res = getAllVtexSiteProductsWithQuery("arroz", 4, True)
print(res)