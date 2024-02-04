class Student:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
    
    def display_info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        
    def change_name(self, new_name: str):
        self.name = new_name
        
s1 = Student()
s1.display_info()
s1.change_name("Rohit")
s1.display_info()
