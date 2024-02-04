"""
 Ask a string from user. Convert all the alphabets to uppercase.

    
"""
my_string = "ABC12345abcd"
result=""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <=122 :
        new_ascii = ascii - 32
        char = chr(new_ascii)
        result += char
    else:
        result += ch

print(result)
# result = my_string.isupper()
# print(result)
