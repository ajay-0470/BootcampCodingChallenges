"""
Coding Challenge 41: Convert Number to Words Using Mathematical Logic
Input : 270176
Output: Two Seven Zero One Seven Six
"""


while True:
    try:
        n = input("Enter the number: ")

     
        if not n.isdigit():
            raise ValueError

        break
    except ValueError:
        print("Invalid input. Please enter digits only.")


digit_words = {
    '0':"zero",
    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':"five",
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"nine"
}

for digit in n:
    print(digit_words[digit],end=" ")