"""
Coding Challenge 39: Printing Pattern of Perfect Squares with Alternating Signs in N
Rows
1
-4 9
-16 25 -36
49 -64 81 -100
.
N rows
"""

while True:
    try:
        n = int(input("Enter the limit: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

num = 1
flag = True
    
for i in range(1, n+1):
    for j in range(i):
        square = num * num
        if flag:
            print(square, end=" ")
        else:
            print(-square, end=" ")
        flag = not flag
        num += 1
    print()

