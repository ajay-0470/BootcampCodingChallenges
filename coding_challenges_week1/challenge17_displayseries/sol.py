"""
Coding Challenge 17: Display the Series 1,2,3,4,5,6...N
"""

while True:
    try:
        n = int(input("Enter the limit: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(1, n + 1):
    print(i)
