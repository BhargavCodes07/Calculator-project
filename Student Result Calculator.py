# Student Result System

def get_valid_marks(subject):
    marks = int(input(f"Enter {subject} marks (0-100): "))

    while marks < 0 or marks > 100:
        print("Invalid input. Marks must be between 0 and 100.")
        marks = int(input(f"Re-enter {subject} marks (0-100): "))

    return marks


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "Fail"


# Input section
chemistry = get_valid_marks("Chemistry")
physics = get_valid_marks("Physics")
maths = get_valid_marks("Maths")

# Grades
chem_grade = get_grade(chemistry)
phy_grade = get_grade(physics)
maths_grade = get_grade(maths)

# Calculations
total = chemistry + physics + maths
percentage = total / 300 * 100

# Overall grade
overall_grade = get_grade(percentage)

# Output
print("\n--- RESULT ---")
print("Chemistry:", chemistry, "| Grade:", chem_grade)
print("Physics:", physics, "| Grade:", phy_grade)
print("Maths:", maths, "| Grade:", maths_grade)

print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Overall Grade:", overall_grade)
