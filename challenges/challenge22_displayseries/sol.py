"""
Coding Challenge 22: Display the Series 1,4,7,12,23...N
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
    
a = 1
b = 4
c = 7


if a <= n:
    print(a)
if b <= n:
    print(b)
if c <= n:
    print(c)

d = a+b+c

while(d<=n):
    print(d)
    a,b,c = b,c,d
    d=a+b+c