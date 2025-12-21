"""
Coding Challenge 38: Fibonacci Series Pattern (N Rows)
1
1 2
3 5 8
13 21 34 55
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

a=1
b=1

for i in range(1,n+1):
    for j in range(i):
        print(a,end=" ")
        a,b=b,a+b
    print()
