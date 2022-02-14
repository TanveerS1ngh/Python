# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.

user_no1 = int(input("Enter a number over 100 > "))
user_no2 = int(input("Enter a number under 10 > "))

print(f"You have to add {user_no2} {user_no1//user_no2} times to make {user_no1}")