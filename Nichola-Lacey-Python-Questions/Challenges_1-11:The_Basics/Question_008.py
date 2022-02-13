# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

Total_Bill = int(input("Enter total amount of bill > "))
Diners = int(input("Enter number of diners > "))

print(f"Each of you must pay > {Total_Bill / Diners}")