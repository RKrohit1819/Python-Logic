"""
 Ask ‘n’ from user. Create a list of last n elements but in reverse order
using slicing.
"""
a = [5,25,63,98,45,78,65,63]
num = int(input("Enter the n number = "))

b = a[-1:-num-1:-1]
print(b)
