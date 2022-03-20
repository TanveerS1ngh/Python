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
nbr = list(range(20))
print(nbr[::4])  # skip the numbers which are not multiple of assign number
# here skip in reverse it print with the gap of 2 numbers and print next number
print(nbr[::-3])

# looping over lists

letteers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

for le in letteers:
    print(le)

# here it gonna enumerate the elements in list and show with tuple eterations
for le in enumerate(letteers):
    print(le)

for le in enumerate(letteers):
    print(le[0])  # accessing index in list

for le in enumerate(letteers):
    print(le[0], le[1])  # it will show index with items

# because this sentex not looks good we'll use list unpacking

# unpacking list[] by putting () we can unpack tuple also
for index, item in enumerate(letteers):
    print(index, item)  # unpack the list

# add and remove items from list

letteers = ["a", "b", "c", "d", "e", "f"]

letteers.remove("b")  # for remove items from list if you dont know index value

print(letteers)


letteers.pop(3)  # for remover of pop items from list using index value

print(letteers)

del letteers[0:2] # using del we can delete items from list or whole list

print(letteers)

letteers.clear() # to remove all the objects from list

print(letteers)

#