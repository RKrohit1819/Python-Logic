"""
 Write a program that prompts the user to specify the length of a list
and then requests numbers to populate that list. Display the final list as
the output.

    
"""
list_length = int(input("Enter length = "))
result = []

for i in range(0,list_length):
    num = int(input("Enter number = "))
    result.append(num)
    
print(result)
    