""" 
Coding Challenge 50: Level 5: Display the number of odd and even numbers from the
array
"""

while True:
    try:
        n = int(input("Enter the size of the array: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print(arr)

odd = 0
even = 0

for i in range(n):
    if(arr[i]%2==0):
        even+=1
    else:
        odd+=1

print("Count of odd numbers is: ",odd)
print("Count of even numbers is: ",even)
