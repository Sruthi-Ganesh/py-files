class Item(object):
    def __init__(self):
        pass
    def calculateSalePrice(self,price):
        self.price = price
        print self.price

class Perishable(Item):
    def __init__(self,price):
        self.price=price
    def calculateSalePrice(self):
        self.price=self.price+500
        super(Perishable,self).calculateSalePrice(self.price)

class NonPerishable(Item):
    def __init__(self,price):
        self.price=price
    def calculateSalePrice(self):
        self.price=self.price+(self.price*0.1)
        super(NonPerishable,self).calculateSalePrice(self.price)

print "ct20162001781",
print "sruthibadal@gmail.com \n"
price = float(raw_input("Enter the price: "))
print "For perishable class the price would be: ",
Perish = Perishable(price)
Perish.calculateSalePrice()
print "For non perishable class the price would be: ",
NonPerishable(price).calculateSalePrice()
