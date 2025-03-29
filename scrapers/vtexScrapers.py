from tools import vtexJsonFinder

def GetCarrefour(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.carrefour.com.ar", debug)
    return prodsRes

def GetJumbo(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.jumbo.com.ar", debug)
    return prodsRes

def GetDia(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://diaonline.supermercadosdia.com.ar", debug)
    return prodsRes

def GetDisco(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.disco.com.ar", debug)
    return prodsRes

def GetVea(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.vea.com.ar", debug)
    return prodsRes


def GetMas(query, cant, debug):
    prodsRes = vtexJsonFinder.GetProds(query, cant, "https://www.masonline.com.ar", debug)
    return prodsRes

