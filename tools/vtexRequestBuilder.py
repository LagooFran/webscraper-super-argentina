import urllib.parse as urlib
import base64 as b64
import json as j

def BuildRequest(query, cant, url, debug):
    
    #junto todos los resultados de las funciones para generar la url final
    #add up all function results to make the final url 

    finalRequest = url + "/_v/segment/graphql/v1" + FormatParams()
    finalRequest += "&variables={}" + "&extensions=" + GetExtensions(query, cant)
    if debug:
        print(finalRequest)

    return finalRequest

def FormatParams():

    #aniadir parametros de la query
    #add query parameters

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

    #dar el formato correcto a los parametros
    #give format to the parameters to comply with url query structure
    

    for item in params:
        if first == True:
            formattedParams += f"{item}={params[item]}" 
            first = False
        else:
            formattedParams += f"&{item}={params[item]}"  

    return formattedParams

def GetExtensions(query, cant):
    
    #variables necesarias para hacer una query a la api que usa vtex
    #neccesary variables for vtex query api

    variables = {
        "count" : cant,
        "fullText" : query,
        "hideUnavailableItems" : True,
        "productOriginVtex" : True,
        "shippingOptions" : [],
        "simulationBehavior" : "default", 
        "variant" : None
    }

    variablesJson = j.dumps(variables, separators=(',',':'))
    variablesEncoded = b64.b64encode(bytes(variablesJson, "utf8"))

    #Extensiones necesarias para hacer una query a la api que usa vtex
    #neccesary extensions for vtex query api

    extensions = {"persistedQuery" : {
        "version" : 1,
        "sha256Hash" : "0ef2c56d9518b51f912c2305ac4b07851c265b645dcbece6843c568bb91d39ff",
        "sender" : "vtex.store-resources@0.x",
        "provider" : "vtex.search-graphql@0.x"
    }, "variables" : str(variablesEncoded.decode()) }

    #las extensiones tienen que estar en formato json y las variables codificadas en base 64
    #extensions need to be in json format and variables need to be encoded in b64 utf8

    extensionsJson = j.dumps(extensions, separators=(',',':'))


    return str(extensionsJson)