"""
Coding Challenge 23: Display the Series 1,5,9,13,21,25,29,37,41...N
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
i = 1

while(term<=n):
    print(term)
    if((i==4)or((i>4)and(((i-4)%3)==0))):
        term+=8
    else:
        term+=4
    i+=1