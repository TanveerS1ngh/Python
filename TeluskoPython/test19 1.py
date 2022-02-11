a=int(input('Enter your 1st number: '))
b=int(input('Enter your 2st number: '))
c=int(input('Enter your 3st number: '))

if a>b and a>c :
  print('greater number is',a)
elif b>c and b>a :
  print('greater number is',b)
elif c>a and c>b :
  print('greater number is',c)
else :
  print ("Wrong input")


