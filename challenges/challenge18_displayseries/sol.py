"""
Coding Challenge 18: Display the Series 1,3,5,7,9...N
"""
while True:
    try:
        n = int(input("Enter the limit: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

for i in range(1, n + 1, 2):
    print(i)
