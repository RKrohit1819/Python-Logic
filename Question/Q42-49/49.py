# Write a program to calculate the sum of all the numbers divisible by 4
# from 20 to 50.
# 20+24+28+....+40+44+48


i=20
total=0
while i<50:
    if i%4==0:
        total=total+i
    i=i+1
print(total)
        


