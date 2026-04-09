class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_available_books(self):
        for book in self.books:
            if not book.is_borrowed:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None