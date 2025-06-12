from Books import book_data

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
    title = book["title"]
    author = book["author"]
    genre = book["genre"]
    year = book["year"]
    book_add = Book(title, author, genre, year)
    library.append(book_add)

class Library:
    def __init__(self, my_library):
        self.books = my_library

    def display_books(self):
        for book in self.books:
            print (f"The {book.title} book of {book.genre} genre is written by {book.author} in {book.year}.")

    def borrow_book(self, book_name, user):
        for book in self.books:
            if book.title == book_name:
                return book.check_out(user)
        return f"{book_name} is not present in the library."

    def return_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                return book.return_book()
            
