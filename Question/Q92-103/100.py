"""

 Make your own list. Find the sum of all numbers divisible by 3 or 4.


"""

my_list= [3,4,5, 200,400, 100,158]
total=0

# Iteration by Index
for i in  range (0, len(my_list)):
    if my_list[i]%3 == 0 and my_list[i]%4==0 :
        total=total+my_list[i]
    
print(total)

#Iteration by Value

# for i in my_list:
#     if i %2==0:
#         count=count+1
#         #print(i, end=" ")
# print(count)
