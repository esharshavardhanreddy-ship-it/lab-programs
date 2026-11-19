
attendance = {}

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name not in attendance:
            attendance[name] = {"Present": 0, "Absent": 0}
            print("Student added successfully!")
        else:
            print("Student already exists!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in attendance:
            status = input("Enter P for Present or A for Absent: ")

            if status.upper() == "P":
                attendance[name]["Present"] += 1
                print("Attendance marked Present.")
            elif status.upper() == "A":
                attendance[name]["Absent"] += 1
                print("Attendance marked Absent.")
            else:
                print("Invalid attendance status!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\n--- ATTENDANCE REPORT ---")

        for name, data in attendance.items():
            total = data["Present"] + data["Absent"]

            if total > 0:
                percentage = (data["Present"] / total) * 100
            else:
                percentage = 0

            print("\nStudent:", name)
            print("Present:", data["Present"])
            print("Absent:", data["Absent"])
            print("Attendance:", round(percentage, 2), "%")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
