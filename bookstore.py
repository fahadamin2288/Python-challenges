# class Book:
#     def __init__(self, book_id, title, author, price, stock):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.price = price
#         self.stock = stock
#
#     def __str__(self):
#         return f"{self.book_id:<5}{self.title:<25}{self.author:<20}${self.price:<10.2f}{self.stock:<10}"
#
#
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
# class Bookstore:
#     def __init__(self):
#         self.books = [
#             Book(1, "The Catcher in the Rye", "J.D. Salinger", 10.99, 5),
#             Book(2, "To Kill a Mockingbird", "Harper Lee", 8.99, 3),
#             Book(3, "1984", "George Orwell", 12.99, 10),
#         ]
#         self.users = {}
#         self.users["admin"] = User("admin", "password123")
#         self.current_user = None
#
#     def authenticate(self):
#         """Handles user authentication."""
#         print("\nUser Authentication")
#         username = input("Username: ")
#         password = input("Password: ")
#
#         if username in self.users:
#             if self.users[username].password == password:
#                 self.current_user = self.users[username]
#                 print("\nLogin successful!\n")
#                 return True
#         print("\nInvalid credentials! Exiting the program.")
#         return False
#
#     def display_books(self):
#         """Displays available books."""
#         print("\nAvailable Books:")
#         print(f"{'ID':<5}{'Title':<25}{'Author':<20}{'Price':<10}{'Stock':<10}")
#         print("-" * 70)
#         for book in self.books:
#             print(book)
#
#     def search_books(self):
#         """Searches for books by title."""
#         query = input("\nEnter book title to search: ").lower()
#         results = []
#         for book in self.books:
#             if query in book.title.lower():
#                 results.append(book)
#
#         if results:
#             print("\nSearch Results:")
#             print(f"{'ID':<5}{'Title':<25}{'Author':<20}{'Price':<10}{'Stock':<10}")
#             print("-" * 70)
#             for book in results:
#                 print(book)
#         else:
#             print("\nNo books found.")
#
#     def purchase_book(self):
#         """Handles book purchase transactions."""
#         self.display_books()
#         try:
#             book_id = int(input("\nEnter the ID of the book to purchase: "))
#             quantity = int(input("Enter the quantity: "))
#
#             for book in self.books:
#                 if book.book_id == book_id:
#                     if book.stock >= quantity:
#                         book.stock -= quantity
#                         total_price = book.price * quantity
#                         print(f"\nPurchase successful! Total price: ${total_price:.2f}")
#                         return
#                     else:
#                         print("\nInsufficient stock.")
#                         return
#             print("\nInvalid book ID.")
#         except ValueError:
#             print("\nInvalid input. Please enter numeric values.")
#
#     def main_menu(self):
#         """Displays the main menu and handles user choices."""
#         while True:
#             print("\nMain Menu")
#             print("1. View Books")
#             print("2. Search Books")
#             print("3. Purchase Book")
#             print("4. Exit")
#
#             choice = input("\nEnter your choice: ")
#
#             if choice == "1":
#                 self.display_books()
#             elif choice == "2":
#                 self.search_books()
#             elif choice == "3":
#                 self.purchase_book()
#             elif choice == "4":
#                 print("\nThank you for visiting the bookstore. Goodbye!")
#                 break
#             else:
#                 print("\nInvalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     bookstore = Bookstore()
#     if bookstore.authenticate():
#         bookstore.main_menu()



class Book:
    def __init__(self, book_id, title, author, price, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.book_id:<5}{self.title:<25}{self.author:<20}${self.price:<10.2f}{self.stock:<10}"

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role  # 'admin' or 'user'

    def __str__(self):
        return f"Username: {self.username}, Role: {self.role}"

class Bookstore:
    def __init__(self):
        self.books = [
            Book(1, "The Catcher in the Rye", "J.D. Salinger", 10.99, 5),
            Book(2, "To Kill a Mockingbird", "Harper Lee", 8.99, 3),
            Book(3, "1984", "George Orwell", 12.99, 10),
        ]
        self.users = {}
        self.users["admin"] = User("admin", "password123", "admin")
        self.current_user = None

    def authenticate(self):
        """Handles user authentication."""
        print("\nUser Authentication")
        username = input("Username: ")
        password = input("Password: ")

        if username in self.users:
            if self.users[username].password == password:
                self.current_user = self.users[username]
                print("\nLogin successful!\n")
                return True
        print("\nInvalid credentials! Exiting the program.")
        return False

    def display_books(self):
        """Displays available books."""
        print("\nAvailable Books:")
        print(f"{'ID':<5}{'Title':<25}{'Author':<20}{'Price':<10}{'Stock':<10}")
        print("-" * 70)
        for book in self.books:
            print(book)

    def search_books(self):
        """Searches for books by title."""
        query = input("\nEnter book title to search: ").lower()
        results = []
        for book in self.books:
            if query in book.title.lower():
                results.append(book)

        if results:
            print("\nSearch Results:")
            print(f"{'ID':<5}{'Title':<25}{'Author':<20}{'Price':<10}{'Stock':<10}")
            print("-" * 70)
            for book in results:
                print(book)
        else:
            print("\nNo books found.")

    def purchase_book(self):
        """Handles book purchase transactions."""
        self.display_books()
        try:
            book_id = int(input("\nEnter the ID of the book to purchase: "))
            quantity = int(input("Enter the quantity: "))

            for book in self.books:
                if book.book_id == book_id:
                    if book.stock >= quantity:
                        book.stock -= quantity
                        total_price = book.price * quantity
                        print(f"\nPurchase successful! Total price: ${total_price:.2f}")
                        return
                    else:
                        print("\nInsufficient stock.")
                        return
            print("\nInvalid book ID.")
        except ValueError:
            print("\nInvalid input. Please enter numeric values.")

    def add_user(self):
        """Adds a new user."""
        print("\nAdd New User")
        username = input("Enter new username: ")
        if username in self.users:
            print("\nUsername already exists. Please choose a different username.")
        else:
            password = input("Enter password: ")
            role = input("Enter role (admin/user): ").lower()
            if role not in ["admin", "user"]:
                role = "user"  # default role
            self.users[username] = User(username, password, role)
            print(f"\nUser '{username}' with role '{role}' added successfully.")

    def delete_user(self):
        """Deletes an existing user."""
        if self.current_user.role == "admin":  # Only admin can delete users
            print("\nDelete User")
            username = input("Enter username to delete: ")
            if username in self.users and username != "admin":
                del self.users[username]
                print(f"\nUser '{username}' deleted successfully.")
            else:
                print("\nCannot delete this user.")
        else:
            print("\nYou don't have permission to delete users.")

    def update_user(self):
        """Allows a user to update their username or password."""
        if self.current_user:
            print(f"Current user: {self.current_user.username}")
            choice = input("Do you want to (1) change username or (2) change password? ")
            if choice == "1":
                new_username = input("Enter new username: ")
                if new_username in self.users:
                    print("\nUsername already exists.")
                else:
                    self.users[new_username] = self.current_user
                    self.users[new_username].username = new_username
                    del self.users[self.current_user.username]
                    self.current_user.username = new_username
                    print(f"\nUsername updated to {new_username}")
            elif choice == "2":
                new_password = input("Enter new password: ")
                self.current_user.password = new_password
                print("\nPassword updated successfully.")
            else:
                print("\nInvalid choice.")
        else:
            print("\nNo user is currently logged in.")

    def main_menu(self):
        """Displays the main menu and handles user choices."""
        while True:
            print("\nMain Menu")
            print("1. View Books")
            print("2. Search Books")
            print("3. Purchase Book")
            if self.current_user and self.current_user.role == "admin":
                print("4. Add User (Admin Only)")
                print("5. Delete User (Admin Only)")
            print("6. Update User Info")
            print("7. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.display_books()
            elif choice == "2":
                self.search_books()
            elif choice == "3":
                self.purchase_book()
            elif choice == "4" and self.current_user and self.current_user.role == "admin":
                self.add_user()
            elif choice == "5" and self.current_user and self.current_user.role == "admin":
                self.delete_user()
            elif choice == "6":
                self.update_user()
            elif choice == "7":
                print("\nThank you for visiting the bookstore. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    bookstore = Bookstore()
    if bookstore.authenticate():
        bookstore.main_menu()
