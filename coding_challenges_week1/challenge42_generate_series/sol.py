"""
Coding Challenge 42: Generate Series - 1, -5, 9, -13, 17, -21, ... N
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

value = 1
sign = 1

while(value<=n):
    print(value*sign,end=" ")
    value+=4
    sign*=-1