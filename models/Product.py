class Product:

    def __init__(self, name="", price="", brand="", pricePUnit="", imgaeUrl=""):
        self.name = name
        self.price = price
        self.pricePUnit = pricePUnit
        self.brand = brand
        self.imageUrl = imgaeUrl

    def ToDict(self):
        prodDict = {
            "name" : self.name,
            "price" : self.price,
            "brand" : self.brand,
            "pricePUnit" : self.pricePUnit,
            "imageUrl" : self.imageUrl
        }
        return prodDict


