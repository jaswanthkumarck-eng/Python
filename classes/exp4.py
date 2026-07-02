class student:
    def __init__(self):
        self.name="name"
        self.regno="921"
    def display(self):
        print("Name:",self.name)
        print("regno:",self.regno)

s1=student()
s2=student()

s1.name="jk"
s1.regno="21"

s2.name="gp"
s2.regno="20"
print(s1.name)
print(s1.regno)
s1.display()
print(s2.name)
print(s2.regno)
s2.display()
