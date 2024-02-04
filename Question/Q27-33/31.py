"""
 Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.


"""

bill_amount=float(input("enter bill = "))

if bill_amount>=50000:
    discount=30
elif bill_amount>=40000 and bill_amount<50000:
    discount=25
elif bill_amount>=30000 and bill_amount<40000:
    discount=20  
elif bill_amount>=20000 and bill_amount<30000:
    discount=10
else:
    discount=0
    
print(f"You got {discount}% discount")

final_bill=bill_amount - (bill_amount*discount/100)
print(f"Your final bill is {final_bill}")
    