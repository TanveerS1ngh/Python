year = int(input("Plz enter the year you want to check = "))

#program to check leap year
if year%400 == 0:
  print ("This is a leap year with 366 Days")
else:
  print ("This is not an leap year it has 365 days")