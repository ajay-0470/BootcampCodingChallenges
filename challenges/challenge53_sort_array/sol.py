"""
Coding Challenge 53: Level 2: Sort the array in ascending or descending order based
on input of user
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
    arr.append(int(input(f"Enter element {i+1}: ")))\
    
choice = input("Enter A for Ascending or D for Descending: ").upper()

if choice == 'A':
    sorted_arr = sorted(arr)
elif choice == 'D':
    sorted_arr = sorted(arr, reverse=True)

print("Sorted array:", sorted_arr)
