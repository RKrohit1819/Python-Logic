#many form

class Animal:
    def sound(self):
        print("Animal speaking")
        
        
class Dog(Animal):
    def sound(self):
        print("Bhaw bhaw bhaw")
        
class cat(Animal):
    def sound(self):
        print("Meow Meow Meow")
        
obj = cat()
obj.sound()
        