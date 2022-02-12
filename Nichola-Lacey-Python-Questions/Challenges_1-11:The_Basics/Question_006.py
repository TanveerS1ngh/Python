# Ask how many slices of pizza the user started with and ask how many slices they have eaten.Work out how many slices they have left and display the answer in a user-friendly format.

total_slices = int(input("Total pizza slices > "))
slices_eaten = int(input("Slices we ate > "))

print(f"Slices left are {total_slices-slices_eaten}")