class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Bird chirps")

a1 = animal()
a1.sound()
d1 = dog()
d1.sound()  
b1 = bird()
b1.sound()