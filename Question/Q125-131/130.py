"""

Ask start and end index from the user. Create a list from start index
to end index using slicing
    
"""
a = [5,25,63,98,45,78,65,63]
start_index = int(input("Enter the start index = "))
end_index = int(input("Enter the end index = "))
b = a[start_index:end_index]
print(b)