income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income*0.18 - 556.02
else:
    tmp = income - 85528
    tax = 14839.02 + tmp*0.32  
if tax < 0:
    tax = 0.0
# Put your code here.
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")