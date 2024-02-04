"""
    
Ask a string from user. Count the number of uppercase and
lowercase characters in that String.

"""
my_string = "Ram is a good boy"

upper_count = 0
lower_count = 0

for ch in my_string:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
        
print(upper_count)
print(lower_count)
    
