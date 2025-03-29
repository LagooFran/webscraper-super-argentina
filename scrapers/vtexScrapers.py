from tools import vtexJsonFinder

def GetCarrefour(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.carrefour.com.ar", debug)
    return prodsRes

def GetJumbo(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.jumbo.com.ar", debug)
    return prodsRes
