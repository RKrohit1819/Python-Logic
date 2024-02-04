"""_
 Make your own list. Print how many positive and negative numbers
are here.

"""
# Creating a list
my_list = [-2, 7, -12, 5, 8, -9, 6, -15, 10, 16]

# Initializing counters
positive_count = 0
negative_count = 0

# Counting positive and negative numbers
for number in my_list:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Printing the result
print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)
