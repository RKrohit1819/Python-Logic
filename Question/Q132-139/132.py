"""
Ask a string from user. Count how many alphabets are there in that
string.
"""

a="Abc123"
count=0
# for ch in a:
#     if ch.isalpha():
#         count = count+1

for ch in a:
    ascii = ord(ch)
    if(ascii>=65 and ascii<90) or (ascii>=97 and ascii<=122):
        count += 1
        
print(count)
    
        
    

print(count)    
    