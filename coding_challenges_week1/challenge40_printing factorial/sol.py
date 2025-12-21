"""
Coding Challenge 40: Printing Pattern of Factorials in N Rows
1
1 2
6 24 120
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

num = 0
fact = 1

for i in range(1,n+1):
    for j in range(i):
        print(fact,end=" ")
        num+=1
        fact*=num
    print()

