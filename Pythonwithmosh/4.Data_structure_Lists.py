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

del letteers[0:2]  # using del we can delete items from list or whole list

print(letteers)

letteers.clear()  # to remove all the objects from list

print(letteers)

# find index of letter in list

letteers = ["a", "b", "c", "d", "e", "f"]

print(letteers.index("d"))

# sorting tuple inside lists using lambda function

item = [("Prd1", 10), ("Prd2", 20), ("Prd3", 50)]

item.sort(key=lambda item: item[1], reverse=True)

print(item)

# map function

items = [("Prd1", 10), ("Prd2", 20), ("Prd3", 50)]

x = map(lambda item: item[0], items)

for item in x:
    print(item)

xx = list(map(lambda item: item[1], items))

print(xx)

# filter function

items = [("Prd1", 10), ("Prd2", 20), ("Prd3", 50)]

x1 = list(filter(lambda item: item[1] >= 20, items))

print(x1)

# list comprehensions

items = [("Prd1", 10), ("Prd2", 20), ("Prd3", 50)]

#x1 = list(filter(lambda item: item[1] >= 20, items))

x2 = [item[1] for item in items]

x3 = [item for item in items if item[1] >= 20]

print(x2, x3)

# zip function

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [10, 20, 30, 40, 50, 60, 70, 80]

x4 = list(zip(list1, list2))

print(x4)

print(list(zip("a,b,c,d,e,f,g,h", list1, list2)))

# stack

# it has behaviour LIFO last in first out


browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

print(browsing_session.pop())
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")

# queues

# in here this has behaviour FIFO first in first out
