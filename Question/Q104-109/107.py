"""
 Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered.
 
"""
a=[5,10,50,25,30,60]
b=[]

for i in a:
    if i%10!=0:
        b.append(i)
        
print(b)