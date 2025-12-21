"""
Coding Challenge 24: Display the Series 1,1,2,3,5,8,13,21...N
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
    if(i==1):
        print(a)
    elif(i==2):
        print(b)
    else:
        c = a+b
        print(c)
        a,b=b,c
    