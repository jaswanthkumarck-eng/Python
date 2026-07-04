class phone():
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)

samsung=phone("Samsung",20000,"Type C")
samsung.display()

realme=phone("Realme",15000,"Type C")
realme.display()
