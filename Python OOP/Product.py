class Product(object):
    def _init_(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def tax(self, taxAmount):
        return self.price + taxAmount
    def returnProduct(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "new":
            self.status = "for sale"
        if reason == "used":
            self.status = "used"
            self.price -= (self.price * 20) / 100
        return self
    def displayInfo(self):
        print "Price {}, Name {}, Weight {}, Brand {}, Status {}".format(self.price, self.name, self.weight, self.brand, self.status)
        return self

product = Product(100, "kouti", 5, "lala")
product.returnProduct("new")
product.displayInfo()