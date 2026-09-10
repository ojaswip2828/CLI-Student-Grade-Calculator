# Student Grade Calculator
# This is a simple CLI program that calculates a student's average
# marks and grade based on the subjects entered by the user.

print("=== Student Grade Calculator ===")

name = input("Enter student name: ")
num_subjects = int(input("How many subjects? "))

total = 0
marks_list = []

for i in range(num_subjects):
    marks = float(input("Enter marks for subject " + str(i + 1) + " (out of 100): "))
    marks_list.append(marks)
    total = total + marks

average = total / num_subjects

# deciding the grade based on average marks
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print("Name:", name)
print("Marks entered:", marks_list)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)

if grade == "F":
    print("You failed. Better luck next time!")
else:
    print("Congratulations, you passed!")
