class Product:

    def __init__(self, name="", price="", brand="", pricePUnit="", unit="" , imgaeUrl="", productUrl=""):
        self.name = name
        self.price = price
        self.pricePUnit = pricePUnit
        self.unit = unit
        self.brand = brand
        self.imageUrl = imgaeUrl
        self.productUrl = productUrl

    def ToDict(self):
        prodDict = {
            "name" : self.name,
            "price" : self.price,
            "brand" : self.brand,
            "pricePUnit" : self.pricePUnit,
            "unit" : self.unit,
            "imageUrl" : self.imageUrl,
            "productUrl" : self.productUrl
        }
        return prodDict


