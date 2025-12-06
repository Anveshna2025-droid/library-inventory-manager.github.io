"""
This is a multiline comment .
This assignment is submitted as lab3 by:
Name- Anveshna
Roll no. - 2501010130 
Course - B.Tech CSE Core (section A)
Submitted to - Feroz Sir
"""

import json

"""Library Management System
Let's create a simple library management system that allows 
users to add books, issue books, return books, and view the inventory of books.
The system will store book information in a JSON file for ease.
"""


class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # "available" or "issued"

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_dict(self):
        """Convert Book object into a dictionary so it can be stored in JSON."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if self.is_available():
            self.status = "issued"
            return True
        return False

    def take_back(self):
        if not self.is_available():
            self.status = "available"
            return True
        return False


""" This is a library class """


class LibrarySystem:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = []
        self.load_from_file()

    def load_from_file(self):
        """Read JSON file and rebuild the list of Book objects."""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book(**b) for b in data]
        except (FileNotFoundError, json.JSONDecodeError):
            # If file is missing or invalid, start with an empty list
            self.books = []

    def save_to_file(self):
        """Write current list of books into JSON file."""
        data = [b.to_dict() for b in self.books]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, isbn):
        book_obj = Book(title, author, isbn)
        self.books.append(book_obj)
        self.save_to_file()
        print("Book added to the system.")

    def issue_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.issue():
                    self.save_to_file()
                    print("Book issued to user.")
                else:
                    print("This book is already out.")
                return
        print("No book found with that ISBN.")

    def return_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.take_back():
                    self.save_to_file()
                    print("Book marked as returned.")
                else:
                    print("This book was not issued.")
                return
        print("No book found with that ISBN.")

    def show_books(self):
        if not self.books:
            print("No books stored yet.")
            return

        print("\n----- Current Library Books -----")
        for b in self.books:
            print(b)
        print("---------------------------------")

    def search_title(self, title_part):
        title_part = title_part.lower()
        results = [b for b in self.books if title_part in b.title.lower()]

        if not results:
            print("No titles matched your search.")
            return

        for b in results:
            print(b)


"""Getting done with main menu , this will be shown to user """


def main():
    system = LibrarySystem()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add a new book")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. Show all books")
        print("5. Search book by title")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author name: ")
            isbn = input("ISBN: ")
            system.add_book(title, author, isbn)

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            system.issue_by_isbn(isbn)

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            system.return_by_isbn(isbn)

        elif choice == "4":
            system.show_books()

        elif choice == "5":
            title = input("Enter part of the title to search: ")
            system.search_title(title)

        elif choice == "6":
            print("Exiting library program. See you soon learner!")
            break
        else:
            print("Invalid choice, please pick a number between 1 and 6.")


if __name__ == "__main__":
    main()
