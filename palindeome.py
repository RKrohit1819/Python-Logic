"""
mom -mom
abc- cba
noon - noon  
    
"""
my_string = input("Enter a string = ")

if my_string == my_string[::-1]:
    print("It is a palindrome")
else:
    print("It is  not a palindrome")