"""
Ask 5 marks from user.
Calculate percentage and print it.

91-100 -> A grade
81-90 -> B grade
71-80 -> C grade
61-70 -> D grade
1 - 60 -> Fail
Invalid

"""
maths=int(input("Enter mark in maths = "))
science=int(input("Enter mark in science = "))
english=int(input("Enter mark in english = "))
hindi=int(input("Enter mark in hindi = "))
history=int(input("Enter mark in history = "))

total=maths+science+english+hindi+history

percentage = (total/500)*100
print(f"Percentage scored = {percentage}")

if percentage>=91 and percentage<=100:
    print("A grade")
elif percentage>=81 and percentage<=90:
    print("B grade")
elif percentage>=71 and percentage<=80:
    print("C grade")
elif percentage>=61 and percentage<=70:
    print("D grade")
elif percentage>=1 and percentage<=60:
    print("Fail")
else:
    print("Invaild ")
