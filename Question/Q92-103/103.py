"""_
    
  Make your own list. Print the smallest number present in that list.

    
    
"""
my_list= [3,4,5, 200,400, 100,158]

# largest=0
smallest = my_list[0]

# Iteration by Index

for i in  range (0, len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]
print(smallest)