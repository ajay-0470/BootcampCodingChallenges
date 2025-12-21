"""
Coding Challenge 59: Write a program to store elements into a M * N matrix of
integer. Display the matrix and its transpose.
"""

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

print("2D Matrix row-wise: ")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


transpose = []

for j in range(n):
    new_row = []
    for i in range(m):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("Transpose matrix: ")
for i in range(n):
    for j in range(m):
        print(transpose[i][j], end=" ")
    print()

