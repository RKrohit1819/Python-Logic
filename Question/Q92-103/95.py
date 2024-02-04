"""
Make your own list. Print all the odd numbers present in the list.
"""
my_list= [3,4,5, 200,400, 100,158]


for i in  range (0, len(my_list)):
    if i%2 == 0:
        print(my_list[i], end=" ")
    
    