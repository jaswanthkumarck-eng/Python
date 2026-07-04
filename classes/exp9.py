class laptop():
    chargertype=" c type"

    def __init__(self):
        self.brand=""
        self.price=34
    
    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
    
hp=laptop()
hp.setprice(50000)
hp.getprice()