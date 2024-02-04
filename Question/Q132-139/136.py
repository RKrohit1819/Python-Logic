"""
Count the number of spaces in a string entered by user.

"""

my_string = " Roh it1253  64acd"

count = 0

for ch in my_string:
    if ord(ch) == 32:
        count += 1
    
print(count)