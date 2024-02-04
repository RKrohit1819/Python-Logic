"""_
    
 Make your own list. Print the largest number present in that list.
    
    
"""
my_list= [-3,-4,-5, -200,-400, -100,-158]

# largest=0
largest = my_list[0]

# Iteration by Index

for i in  range (0, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)