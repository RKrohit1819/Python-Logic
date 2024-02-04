"""
Generate a list of list using list comprehension where format should
be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]].    
    
"""

# Using list comprehension to generate a list of lists
result_list = [[i, "ODD" if i % 2 != 0 else "EVEN"] for i in range(1, 4)]

print(result_list)







