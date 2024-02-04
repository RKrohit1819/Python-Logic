"""_
. Ask a string from user. Convert all the alphabets to lowercase.

"""

my_string = "RAMAN"


my_string = "ABC12345abcd"
result=""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <=90 :
        new_ascii = ascii + 32
        char = chr(new_ascii)
        result += char
    else:
        result += ch

print(result)
# result = my_string.islower()
# print(result)
