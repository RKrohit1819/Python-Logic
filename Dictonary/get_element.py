my_dict = {
    "name": "Rohit",
    "age": 21,
    "gender":"Male",
}

k = input("Enter a key = ")
result = my_dict.get(k)

if result is not None:
    print(result)
else:
    print(" Key does not exits ")


#to get a value
# r = my_dict.get("namee")
# print(r)
# print(type(r))

# print(my_dict["name"])
# print(my_dict["Age"])
# print(my_dict["gender"])