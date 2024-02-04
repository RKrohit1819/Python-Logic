"""
Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence

"""
my_list = [5, 1, "code and debug", 56.32, 5,5 ,"Rohit",1 , 1 ,"Rohit"]
result= []

for num in my_list:
    if num not in result:
        result.append(num)
        
highest_occ_element = 0
highest_occurence =0

for num in  result:
    c = my_list.count(num)
    print(f"{num} occurs {c} times")
    if c > highest_occurence:
        highest_occurence =c 
        highest_occ_element =num
        
print(f"Highest occurence element ={highest_occ_element}")

