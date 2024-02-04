"""
    
Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.

"""
    
num1=int(input("Enter value of num1 = "))    
num2=int(input("Enter value of num2 = ")) 
num3=int(input("Enter value of num3 = ")) 
num4=int(input("Enter value of num4 = ")) 


if num1<num2 and num1<num3 and num1<num4:
    print("num1 is the smallest ")
elif num2<num2 and num2<num3 and num2<num4:
    print("num2 is the smallest ")
elif num3<num2 and num3<num3 and num3<num4:
    print("num3 is the smallest ")
else:
    print("num4 is the smallest")
    