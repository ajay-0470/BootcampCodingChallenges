"""
Coding Challenge 36: Printing number Increasing Pattern (N Rows)
1
22
333
4444
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
    print(f"{i}"*i)
