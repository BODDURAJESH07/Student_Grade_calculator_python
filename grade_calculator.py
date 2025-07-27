# Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

name = input("Enter Student Name: ")
num_subjects = int(input("Enter number of subjects: "))

total = 0
for i in range(num_subjects):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    total += mark

average = total / num_subjects
percentage = (total / (num_subjects * 100)) * 100
grade = calculate_grade(percentage)

print("\n----- RESULT -----")
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
