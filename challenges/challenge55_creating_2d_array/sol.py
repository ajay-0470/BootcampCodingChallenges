"""
Coding Challenge 55: Write a program to create a 2D array and display its elements
row-wise
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

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()