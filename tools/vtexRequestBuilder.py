def BuildRequest(query, site, url):
    return


def GetExtensions():
    return

def FormatParams():
    #Si se necesitara un cambio en los parametros modificar aqui.
    params = {
        "workspace" : "master",
        "maxAge" : "medium",
        "appsEtag" : "remove",
        "domain" : "store",
        "locale" : "es-AR",
        "operationName" : "productSuggestions"
    }
    
    first = True
    formattedParams = "?"

    #dar formato a los parametros para ser utilizados en link

    for item in params:
        if first == True:
            formattedParams += f"{item}={params[item]}" 
            first = False
        else:
            formattedParams += f"&{item}={params[item]}"  

    return formattedParams