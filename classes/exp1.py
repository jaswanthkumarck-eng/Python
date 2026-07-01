class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("sea beach")

jk = goa()
gp = goa()

jk.name="JK"
gp.name="GP"

jk.drink="yes"
gp.drink="no"

print(jk.name)
print("drink:",jk.drink)
print(gp.name)
print("drink:",gp.drink)

jk.party()
gp.beach()
