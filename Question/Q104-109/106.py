"""
 Remove all the even numbers from the list.
    
    
"""
a=[45,65,12,32,99,87]
b=[]

for i in a:
    if i%2==1:
        b.append(i)
        
print(b)