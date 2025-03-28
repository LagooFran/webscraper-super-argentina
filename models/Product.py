class Product:
    name = ""
    price = ""
    pricePUnit = ""
    brand = ""

    def __init__(self, name, price, brand, pricePUnit):
        self.name = name
        self.price = price
        self.pricePUnit = pricePUnit
        self.brand = brand

    def ToDict(self):
        prodDict = {
            "name" : self.name,
            "price" : self.price,
            "brand" : self.brand,
            "pricePUnit" : self.pricePUnit
        }
        return prodDict


