"""
Coding Challenge 19: Display the Series 4,16,36,64...N
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

for i in range(2, n + 1, 2):
    square = i * i
    if square <= n:
        print(square)
