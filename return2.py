"""
Ask 2 number from user.
calculate total of 2 numbers
print if the sum is odd or even
    
"""
def addition(num1, num2):
    total =num1+num2
    print(total)
    return total

def check(num):
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")

x = int(input("Enter the num1 = "))
y = int(input("Enter the num2 = "))

s= addition(x,y)
check(s)




