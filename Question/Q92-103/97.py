"""
Make your own list. Count the number of even numbers present in
that list.

"""

my_list= [3,4,5, 200,400, 100,158]
count=0

# Iteration by Index
# for i in  range (0, len(my_list)):
#     if my_list[i]%2 == 0:
#         print(my_list[i], end=" ")
    
#     print(" ")

#Iteration by Value

for i in my_list:
    if i %2==0:
        count=count+1
        #print(i, end=" ")
print(count)