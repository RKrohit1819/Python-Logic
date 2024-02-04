my_string = "hello World How Are You"
words = my_string.split()

result = "_".join(i.lower() for i in words)
print(result).