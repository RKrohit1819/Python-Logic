"""
 Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string. 
"""

my_string = input("Enter a string: ")
digit = 0
space = 0
symbol = 0
alpha = 0

for ch in my_string:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    elif not ch.isalnum():  # Check if the character is not alphanumeric (symbol)
        symbol += 1

print("Alphabets:", alpha)
print("Digits:", digit)
print("Spaces:", space)
print("Symbols:", symbol)
