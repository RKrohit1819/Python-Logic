"""
 Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user.    
    
"""

my_list = [56,78,56,86,21,21,]
old = int(input("Enter old number ="))
new = int(input("Enter new nubmer ="))
for i in range (0,len(my_list)):
    if my_list[i]==old:
        my_list[i]=new
        
    print(my_list)