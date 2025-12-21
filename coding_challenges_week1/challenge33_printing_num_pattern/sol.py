"""
Coding Challenge 33: Printing Number Pattern (N Rows)
11111
22222
33333
44444
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
    print(f"{i}{i}{i}{i}{i}")