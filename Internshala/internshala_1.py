capacity=20000
cost=3400

customer = int(input('How much mAh you want = '))
cuscost = int(input('Price range = '))


if customer <= capacity:
  if cuscost >= cost :
    print("\nyes we have %dmAh for you"%(customer))
    print("it's cost is %d"%(cost))
    print('Yes, this power bank is for you!')
  else:
    print("No, this doesn't suit your needs.")

else:
  print("Thanks for coming")
