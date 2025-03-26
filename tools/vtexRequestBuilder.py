import urllib.parse as urlib
import base64 as b64
import json as j

def BuildRequest(query, url):
    
    finalRequest = url + "/_v/segment/graphql/v1" + FormatParams()
    finalRequest += "&variables={}" + "&extensions=" + GetExtensions(query)

    return finalRequest

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

def GetExtensions(query):
    #json pre armado
    variables = {
        "count" : 4,
        "fullText" : query,
        "hideUnavailableItems" : True,
        "productOriginVtex" : True,
        "shippingOptions" : [],
        "simulationBehavior" : "default", 
        "variant" : None
    }

    variablesJson = j.dumps(variables, separators=(',',':'))
    variablesEncoded = b64.b64encode(bytes(variablesJson, "utf8"))

    extensions = {"persistedQuery" : {
        "version" : 1,
        "sha256Hash" : "0ef2c56d9518b51f912c2305ac4b07851c265b645dcbece6843c568bb91d39ff",
        "sender" : "vtex.store-resources@0.x",
        "provider" : "vtex.search-graphql@0.x"
    }, "variables" : str(variablesEncoded.decode()) }

    
    extensionsJson = j.dumps(extensions, separators=(',',':'))


    return str(extensionsJson)