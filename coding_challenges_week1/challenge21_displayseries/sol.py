"""
Coding Challenge 21: Display the Series 1,4,9,25,36,49,81...N
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

for i in range(1,int(n**0.5)+1):
    if(i%4!=0):
        print(i*i)

