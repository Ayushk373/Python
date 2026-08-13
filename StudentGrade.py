print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
physics = float(input("Enter Physics marks: "))
english = float(input("Enter English marks: "))
data_structures = float(input("Enter Data Structures marks: "))

total = maths + python + physics + english + data_structures
percentage = total / 5

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
