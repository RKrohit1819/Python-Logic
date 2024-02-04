"""
. Write a Python code to find the second largest element in a list
without sorting
    
"""

my_list = [54,32,17,67,43,11,87,44,54,32]
largest = float("-inf")
second_largest = float("-inf")

for num in my_list:
    if num> largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num <largest:
        second_largest = num
print(second_largest)
