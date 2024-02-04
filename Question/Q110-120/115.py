"""
Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.


"""

my_list1 = [1,2,3,4,5,6,7,8]
my_list2 = [6,7,8,9,10]
result =[]

for num in my_list1:
    if num in my_list2:
        if num not in result:
            result.append(num)
print(result)