"""
Make a list of your own. And remove all the duplicates element from
that list.

    
"""
my_list = [5, 1, "code and debug", 56.32, 5,5 ,"Rohit",1 , 1 ,"Rohit"]
result =[]

for num in my_list:
    if num not in result:
        result.append(num)
        
print(result)
