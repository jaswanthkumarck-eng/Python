class dad():
    def money(self):
        print("dad money")
class land():
    def must(self):
        print("land must")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()

s1=son1()
s1.money()
s1.must()