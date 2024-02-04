"""
Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order.
 
    
"""
my_list=[]
for i in range(5):
    value = int(input(f"Enter value at index {i} = "))
    my_list.append(value)
    
result=[]
for i in range(len(my_list)-1,-1,-1):
    result.append(my_list[i])
print(result)
