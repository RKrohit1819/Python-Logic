"""_
 Make your own list. Print all the even numbers present in the list
 
"""
my_list= [3,4,5, 200,400, 100,158]

# Iteration by Index
# for i in  range (0, len(my_list)):
#     if my_list[i]%2 == 0:
#         print(my_list[i], end=" ")
    
#     print(" ")

#Iteration by Value

for i in my_list:
    if i %2==0:
        print(i, end=" ")
