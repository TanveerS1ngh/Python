# Lists [] syntax and ways to declare list

from sys import getsizeof
from array import array
from collections import deque
from email.headerregistry import UniqueSingleAddressHeader
from enum import unique
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


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()

print(queue)

if not queue:
    print("empty queue")

# Tuples use () syntax

# its an read only list use it to contain sequence of objects we can't add, remove and modify from it ever without () python see it as tuple

# but to define empty tuple use "point = ()"

point = 1, 2, 3, 4, 5
print(point)


point = (1, 2, 3, 4, 5) + (6, 7, 8, 9, 10)  # concatenate the tuple

print(point)

point = (1, 2, 3, 4, 5) * 3  # multiple the tuple

print(point)

point = tuple([1, 2, 3, 4, 5])  # convert list into tuple using tuple function

print(point)

point = (1, 2, 3, 4, 5)

# acess indvidual item like list in range or any way like list
print(point[2:4])

v, w, x, y, z = point  # unpack tuple

print(point)

if 6 in point:
    print("exists")
else:
    print("Bhak ! Pagal h kya ")

# Array it also need typecode


numbers = array("i", [1, 2, 3, 4, 5, 6])  # here "i" is an typecode
numbers.pop(2)
print(numbers)

# Sets use {} set is use to remove duplicate items

numbers = [1, 1, 2, 3, 3, 3, 3, 3, "a", "a", "a", "b", "c", "c", "c", "c"]

print(set(numbers))

# dictionary {"a":1, "b":2, "c":3} use this syntax

point = {"a": 1, "b": 2, "c": 3}

print(point)

point = dict(x=1, y=22, z=333)

print(point["y"])

print(point.get("b", 7888))

# dictionary comprehensions

values = []
for x in range(5):
    values.append(x*2)
print(values)
# [expression for item in items]

values = [x*2 for x in range(5)]  # it's same as upper loop in line 255 to 227

print(values)

# we can also use them in sets and others too... just change [] to {}

values = {x*2 for x in range(5)}  # sets

print(values)

values = {x: x*2 for x in range(5)}  # dictionary

print(values)


# Generator expressions here we dont store data in memory

values = (x*2 for x in range(1001))
print(values)
for x in values:
    print(x)


# without saving data in memory 104 size

values = (x*2 for x in range(1001))
print("gen:", getsizeof(values))

# list data saved in memory 8856 size

values = [x*2 for x in range(1001)]
print("list:", getsizeof(values))

# sets data saved in memory 32984 size

values = {x*2 for x in range(1001)}
print("Sets:", getsizeof(values))

# unpacking operator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*numbers) # * is used for unpacking the list of numbers
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
