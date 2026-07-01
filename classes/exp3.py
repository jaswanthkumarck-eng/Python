class laptop:

    def __init__(self):
        self.price=0
        self.processor=""
        self.ram=""

    def display(self):
        print("Price:",self.price)
        print("Processor:",self.processor)
        print("RAM:",self.ram)

hp=laptop()
hp.price=50000
hp.processor="i5"
hp.ram="16GB"
print(hp.price)
print(hp.processor)
print(hp.ram)
