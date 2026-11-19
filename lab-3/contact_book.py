
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {"name": name, "phone": phone}
        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for c in contacts:
                print("Name:", c["name"])
                print("Phone:", c["phone"])

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["name"].lower() == name.lower():
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        for c in contacts:
            if c["name"].lower() == name.lower():
                contacts.remove(c)
                print("Contact deleted!")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice!")
