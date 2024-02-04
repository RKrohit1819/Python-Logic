class Student:
    
    
    def __init__(self):
        self.name = input("Enter name =")
        self.age = input("Enter age =")
        self.gender = input("Enter gender =")
        self.roll_no = input("Enter roll_no =")

    def info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
    
        
    
s1 = Student()
s1.info()
s2 = Student()
s2.info()

