class Product:
    name = ""
    price = ""
    pricePUnit = ""

    def __init__(self, name, price, pricePUnit):
        self.name = name
        self.price = price
        self.pricePUnit = pricePUnit

    def ToDict(self):
        prodDict = {
            "name" : self.name,
            "price" : self.price,
            "pricePUnit" : self.pricePUnit
        }
        return prodDict


