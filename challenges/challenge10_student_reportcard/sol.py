"""
Coding Challenge 10: Student Report Card Problem
Write a program to accept a student’s name and scores in three subjects. Display the total, average,
and class secured based on the following criteria:
• 1st Class: Average score of 60 and above.
• 2nd Class: Average score of 50 and above.
• Pass Class: Average score of 35 and above.
• Fail: Average score less than 35.
"""

scores = []

name = input("Enter the name of the student ")

for i in range(3):
    num = int(input(f"Enter subject {i+1} score in range of 0-100  "))
    scores.append(num)

total = sum(scores)

average = total/len(scores)

print("Student name: " + name)
print("Total Marks: "+ str(total))
print("Average Marks: "+ str(average))
if(average>=60):
    print("Grade: First Class")
elif(average>=50):
    print("Grade: Second Class")
elif(average>=35):
    print("Grade: Pass Class")
else:
    print("Grade: Fail")

