class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("Name:",self.name)
        print("regno:",self.reg)

t1=teacher("jk","21")
t2=teacher("gp","20")

t1.display()    
t2.display()