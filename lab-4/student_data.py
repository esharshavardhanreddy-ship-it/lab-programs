
# Student Data Manager

while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + usn + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                print("\n--- STUDENT DETAILS ---")
                for line in file:
                    name, usn, marks = line.strip().split(",")
                    print("Name:", name)
                    print("USN:", usn)
                    print("Marks:", marks)
                    print("-------------------")

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        print("Exiting Student Data Manager.")
        break

    else:
        print("Invalid choice!")
