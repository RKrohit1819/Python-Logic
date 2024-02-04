"""_
. Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1.
    
    
"""

my_list = [5, 1, "code and debug", 56.32, 5,5 ,"Rohit",1 , 1 ,"Rohit"]

value = int(input("Enter value= "))

if value in my_list:
    index = my_list.index(value)
    print(f"Index = {index}")
else:
    print(-1)