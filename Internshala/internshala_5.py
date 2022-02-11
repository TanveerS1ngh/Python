#Write a program to print the multiplication of any table using the 'while' loop.
t=400
#p1
Tal = int(input("Table you want to see = "))
a=1
while a <= t:
  C = Tal*a
  print (C)
  a=a+1

#p2
Table = int(input("Table you want to see again = "))
h=1
while h <= t:
  print("{}" .format(Table*h))
  h=h+1
