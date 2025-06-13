from Books import book_data
from tabulate import tabulate
import os

library = []

class Book:
    def __init__(self, title, author, genre, year):
        #Once the code is done, learn the ** method for unpacking
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = True
        self.user = ""

    def __str__(self):
        return f"The {self.title} book of {self.genre} genre is written by {self.author} in {self.year}."
    
    def check_out(self, user):
        if self.available == False:
            return "This book has already been lent to a patron."
        else:
            self.available = False
            self.user = user
            return f"The {self.title} book has been lent to {self.user}"

    def return_book(self):
        self.available = True
        self.user = ""
        return f"Library has received the {self.title} book."

for book in book_data:
    # title = book["title"]
    # author = book["author"]
    # genre = book["genre"]
    # year = book["year"]
    # book_add = Book(title, author, genre, year)
    book_add = Book(**book)  # ✅ Dictionary unpacking
    library.append(book_add)

class Library_setup:
    def __init__(self, my_library):
        self.books = my_library

    def display_books(self):
        for book in self.books:
            print (f"The {book.title} book of {book.genre} genre is written by {book.author} in {book.year}.")

    def borrow_book(self, book_name, user):
        for book in self.books:
            if book.title.lower() == book_name.lower():
                return book.check_out(user)
        return f"{book_name} is not present in the library."

    def return_book(self, book_name):
        for book in self.books:
            if book.title.lower() == book_name.lower():
                return book.return_book()
            
#Write the main loop        

my_library = Library_setup(library)
os.system("clear")

print("Welcome to the library.")
user = input("Please enter your name: ").lower().strip()

while True:
    print("1. View all books.\
           2. Borrow a book \
           3. Return a book\
           4. Exit ")

    try:
        choice = int(input("Please select an option (1–4): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice in (1,2,3,4):
        if choice == 1:
            table_data = []
            for book in my_library.books:
                status = "Available" if book.available else f"Lent to {book.user}"
                table_data.append([book.title, book.genre, book.author, book.year, status])
    
            headers = ["Title", "Genre", "Author", "Year", "Status"]
            print("\nBook Catalog:\n")
            print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        elif choice == 2:
            borrow_book_name = input("Please enter the name of the book you want to borrow: ").lower().strip()
            print(my_library.borrow_book(borrow_book_name, user))
        elif choice == 3:
            return_book_name = input("Please enter the name of the book you want to return: ").lower().strip()
            print(my_library.return_book(return_book_name))
        elif choice == 4:
            break
    else: 
        print("Invalid option selected.")