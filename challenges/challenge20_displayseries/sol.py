"""
Coding Challenge 20: Display the Series 1,2,4,7,11,16,22...N
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

term = 1
increment = 1

while term<=n:
    print(term)
    term+=increment
    increment+=1