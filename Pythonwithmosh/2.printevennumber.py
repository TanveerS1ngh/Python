# for prime numbers

con = 0
for number in range(1, 11):
    if number % 2 == 0:
        con += 1
        print(number)

print("total prime numbers are ", con)
