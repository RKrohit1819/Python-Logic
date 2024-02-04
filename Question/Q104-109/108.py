"""
 Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.    
    
"""

my_list = [1,25,65,46,99,3,4,5]

odd=[]
even=[]

# for i in range(0,len(my_list)):
#     if my_list[i]%2==0:
#         even.append(my_list[i])
#     else:
#         odd.append(my_list[i])

for num in my_list:
    if num %2 ==0:
        even.append(num)
    else:
        odd.append(num)
        
print(f"Even list = {even}")
print(f"Odd list = {odd}")



    