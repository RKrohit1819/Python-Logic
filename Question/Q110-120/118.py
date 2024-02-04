"""
. Write a program to find and print all prime numbers within a given
list.
    
"""

my_list=[2,5,7,8,9,10,11,13,17]
for num in my_list:
    factors = 0
    for i in range(1, num+1):
        if num % i ==0:
            factors += 1
    if factors==2:
        print(num)
            