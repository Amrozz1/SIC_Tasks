from backend import Book

books = {}

def main_menu():
    while True:
        print("\n📚 Book Management System")
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Update a book")
        print("4. Add a review")
        print("5. Show all reviews")
        print("6. Show overall review for a book")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            id = int(input("Book ID: "))
            name = input("Book Name: ")
            field = input("Field: ")
            num_pages = int(input("Number of Pages: "))
            writer = input("Writer: ")
            publisher = input("Publisher: ")
            publish_year = int(input("Publish Year: "))
            is_borrowed = input("Is borrowed? (yes/no): ").lower() == "yes"
            borrow_price = float(input("Borrow Price: "))
            rate = float(input("Rate: "))
            books[id] = Book(id, name, field, num_pages, writer, publisher, publish_year, is_borrowed, borrow_price, rate)

        elif choice == "2":
            if not books:
                print("No books in the system.")
            else:
                for b in books.values():
                    b.show()
                    print("-" * 30)

        elif choice == "3":
            id = int(input("Enter book ID to update: "))
            if id in books:
                field_to_update = input("What do you want to update? ")
                books[id].updater(field_to_update)
            else:
                print("Book not found.")

        elif choice == "4":
            id = int(input("Enter book ID: "))
            if id in books:
                review = input("Enter review: ")
                Book.add_review(id, review)
            else:
                print("Book not found.")

        elif choice == "5":
            Book.show_reviews()

        elif choice == "6":
            id = int(input("Enter book ID: "))
            Book.show_overall(id)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run interface
main_menu()