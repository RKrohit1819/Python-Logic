"""
 Implement a python program to get the last 'n' elements from a list
using slicing.
"""
a = [5,25,63,98,45,78,65,63]
num = int(input("Enter the n number = "))

b = a[-num::]
print(b)

