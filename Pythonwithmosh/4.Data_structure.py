# Lists [] syntax and ways to declare list

word = ["a", "b", "c", "d", "e", "f", "g", "h"]
matrix = [[2, 8], [6, 9], [5, 7]]
lst = [1] * 100  # dup the list values using *
char = list("hello world")
print(word + lst + char)

# accessing items in list

latr = ["a", "b", "c", "d", "e", "f"]
latr[2] = "C"  # change or updating items in list while previous one will remain there
print(latr[1:5])
print(latr[:5])
print(latr[0:])
pint