"""
Coding Challenge 60: Multiply two matrices
"""


m = int(input("Enter number of rows of Matrix A: "))
n = int(input("Enter number of columns of Matrix A: "))

p = int(input("Enter number of columns of Matrix B: "))

print("Enter elements of Matrix A:")
A = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(n):        
    row = []
    for j in range(p):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)


result = []
for i in range(m):
    result.append([0] * p)


for i in range(m):
    for j in range(p):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]


print("Resultant Matrix (A × B):")
for row in result:
    for val in row:
        print(val, end=" ")
    print()
