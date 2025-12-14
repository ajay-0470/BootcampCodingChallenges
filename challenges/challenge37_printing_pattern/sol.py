"""
Coding Challenge 37: Printing number Increasing Pattern (N Rows)
1
12
123
1234
.
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

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{j}",end="")
    print("")
