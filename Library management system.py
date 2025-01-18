from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return f"{self.title} by {self.author}"


class Book(Item):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

    def get_type(self):
        return "Book"


class Magazine(Item):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def get_type(self):
        return "Magazine"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"'{title}' has been removed from the library.")
                return
        print(f"Item with title '{title}' not found in the library.")

    def search_item(self, title):
        for item in self.items:
            if item.title == title:
                print(f"Item found: {item}")
                return
        print(f"Item with title '{title}' not found in the library.")

    def display_items(self):
        print("Items available in the library:")
        for item in self.items:
            print(item)


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.available:
            self.borrowed_items.append(item)
            item.available = False
            print(f"{self.name} has borrowed '{item.title}'")
        else:
            print(f"Sorry, '{item.title}' is not available for borrowing.")

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.available = True
            print(f"{self.name} has returned '{item.title}'")
        else:
            print(f"{self.name} does not have '{item.title}' borrowed.")


def main():
    library = Library()

    # Sample data
    book1 = Book("Python Programming", "John Smith", "123456789")
    book2 = Book("Machine Learning", "Jane Doe", "987654321")
    magazine = Magazine("National Geographic", "Various Authors", "March 2022")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine)

    member = Member("Alice")

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Search Item\n4. Display Items")
        print("5. Borrow Item\n6. Return Item\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            item_type = input("Enter item type (book/magazine): ")
            if item_type.lower() == "book":
                isbn = input("Enter ISBN: ")
                item = Book(title, author, isbn)
            elif item_type.lower() == "magazine":
                issue = input("Enter issue: ")
                item = Magazine(title, author, issue)
            else:
                print("Invalid item type.")
                continue
            library.add_item(item)

        elif choice == "2":
            title = input("Enter title of item to remove: ")
            library.remove_item(title)

        elif choice == "3":
            title = input("Enter title of item to search: ")
            library.search_item(title)

        elif choice == "4":
            library.display_items()

        elif choice == "5":
            title = input("Enter title of item to borrow: ")
            for item in library.items:
                if item.title == title:
                    member.borrow_item(item)
                    break
            else:
                print(f"Item with title '{title}' not found in the library.")

        elif choice == "6":
            title = input("Enter title of item to return: ")
            for item in library.items:
                if item.title == title:
                    member.return_item(item)
                    break
            else:
                print(f"Item with title '{title}' not found in the library.")

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
