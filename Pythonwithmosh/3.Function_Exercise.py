# fizzbuzz algorithm

def fizzbuzz(input):
	if (input % 3 == 0) and (input % 5 == 0):
		return "fizzbuzz"
	elif input % 3 == 0:
		return "fizz"
	elif input % 5 == 0:
		return "buzz"
	
	return input


print(fizzbuzz(int(input("Enter number which is Divisible to 3 and 5 >>> "))))
