
import pickle

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

s = Student("Rohit", 22)

with open('name.txt', 'wb') as f:
    pickle.dump(s, f)

  

        

# Write
# x = "Code and Debug"
# with open("name.txt", "w") as f:
#     f.write(x)

#Read
# with open("name.txt", "r")as f:
#     print(f.read())