"""
Coding Challenge 56: Create a program to compute the sum of all elements in a 2D
array.
"""


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

print("2D Array row-wise: ")

total = 0

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
        total+=matrix[i][j]
    print()

print("Sum of 2D Array is: ",total)