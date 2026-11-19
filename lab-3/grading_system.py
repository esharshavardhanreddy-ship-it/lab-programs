
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")

    m1 = int(input("Enter marks in Subject 1: "))
    m2 = int(input("Enter marks in Subject 2: "))
    m3 = int(input("Enter marks in Subject 3: "))

    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    students[name] = {
        "Total": total,
        "Average": average,
        "Grade": grade
    }

print("\n--- STUDENT RESULTS ---")

for name, details in students.items():
    print("\nName:", name)
    print("Total Marks:", details["Total"])
    print("Average:", round(details["Average"], 2))
    print("Grade:", details["Grade"])
