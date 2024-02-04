"""
. A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
Take following input from user
QUESTIONS 23-26
IF - ELSE
info@codeanddebug.in Code and Debug codeanddebug.in
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not

"""

class_held=int(input("Enter the total class held = "))
class_attended=int(input("Enter class attended = "))

class_per=(class_attended/class_held)*100

print(f"Percentage of class attented = {class_per:4f}%")

if class_per>=75:
    print("yes you can sit in exam ")
else:
    print("No, You cannot sit in exam")