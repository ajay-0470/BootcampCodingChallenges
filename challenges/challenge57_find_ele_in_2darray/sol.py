"""
Coding Challenge 57: Write a program to check if a given element exists in a 2D array
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
    
while True:
    try:
        key = int(input("Enter element to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

found = False

for i in range(rows):
    for j in range(cols):
        if(matrix[i][j]==key):
            found = True
            break      

if(found):
    print("Element found")
else:
    print("Element not found")