class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,department):
        super().__init__("John",50000)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

m1 = manager("ai")
m1.display()