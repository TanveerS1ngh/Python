print("hello world")


# variables

X = "clown"
print(X)
print(type(X))

# for print value we use

print("hello world")

# for print multiple line we use

print('''hi my name is this
              i'm from there
              i go there''')

# Use the f - string in the print Statement

var1 = 123
var2 = 'World'
print(f'Hello to the {var2} {var1}')

# Use the String Formatting With the Help of {}

var1 = 123
var2 = 'World'
print("Hello to the {} {}".format(var2, var1))

# Use a Comma, to Separate the Variables and Print Them

var1 = 'World'
print("Hello to the", var1)

# Use the String Formatting With the Help of %

var1 = 123 # %d for numeric value
var2 = 'World' # %s for string value
print("Hello to the %s %d " % (var2, var1))

# Use the + Operator to Separate Variables in the print Statement

var1 = 123
var2 = 'World'
print('Hello to the {} {}' + var2 + str(var1))

# Print Quotation Marks in Python

a = "Double Quotation Marks: \"\""
b = 'Single Quotation Marks: \'\''
print(a)
print(b)

# strings
MESSAGE = '''for long print like paragraph'''
print(len(MESSAGE))
print(len(MESSAGE[1]))
print(len(MESSAGE[-1]))
print(len(MESSAGE[0:5]))
print(len(MESSAGE[:3]))
print(len(MESSAGE[:]))

# escape sequences
# \"
# \'
# \\
# \n

# string expressions

A = "kami"
B = 5
X = f"{A} {B}"
print(X)

# string methods
name = "clown Singh    "
len(name)

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.find("own"))
print(name.replace("c", "s"))
