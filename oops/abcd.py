import pickle

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

#s = Student("Rohit", 22)

f = open('name.txt',"rb")
st = pickle.load(f)
f.close()

print(st.name)
print(st.age)
