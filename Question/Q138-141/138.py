# write a program to reverse the order word

my_string = "python is good"
words = my_string.split()


words = words[::-1]

result = " ".join(i for i in words)
print(result)