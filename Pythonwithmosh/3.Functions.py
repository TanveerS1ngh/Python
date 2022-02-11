# Create simple Function

def new():
	print("stay away from me bitch")


new()


# Create argument function

def name(first, last):
	print(f"hi {first}")
	print(f"hi {last}")


name("clown", "singh")


# Create return function

def tell_name(first, last):
	return f"{first} {last}"


urname = tell_name("boss", "god")

print(urname)


# make parameter optional and this O.parameter always come at last position

def tell_nam(first, last = ""):
	return f"hi {first} {last}"


print(tell_nam("kami"))
print(tell_nam("kami", "god"))


# create keyword argument function

def increment(num, by):
	return num + by


print(increment(8, 10))


# create single parameter for multiple argument here we replace multiple parameters with single parameter

def gunaha(*numbr):  # this consider input as tuple and use for loop
	total = 1
	for numbr in numbr:
		total *= numbr
	return total


print(gunaha(6, 5, 8, 9))


# when we use '**' we can pass multiple key value pairs consider/package data as dictionary data

def man(**usr):
	print(usr)  # for print all values
	print(usr["name"])  # for print only one value


man(no = 1, name = "ramu", age = 42)
