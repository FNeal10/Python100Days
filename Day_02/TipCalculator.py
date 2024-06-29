print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill.? $"))
tip = int(input("How much tip you want ot give.? 10, 12 or 15.? "))/100
billSplit = int(input("How many people to split the bill.? "))

to_pay_each = (totalBill + tip) / billSplit
final_amount = round(to_pay_each,2)

print(f"Each person should pay: {final_amount}")

