
# Library Management System

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"name": book, "status": "Available"})
        print("Book added successfully!")

    def display_books(self):
        print("\n--- LIBRARY BOOKS ---")

        for book in self.books:
            print("Book:", book["name"])
            print("Status:", book["status"])

    def issue_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        name = input("Enter book name to issue: ")
        library.issue_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "5":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice!")
