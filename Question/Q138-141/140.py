"""
Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should become


"""


my_string = "Python is good"
words = my_string.split()

result = " ".join(i[::-1] for i in words)
print(result)