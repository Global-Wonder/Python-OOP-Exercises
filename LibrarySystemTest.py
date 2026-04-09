from LibrarySystem import Book, User, Library 
    
def main():
    # Create library
    library = Library()

    # Create books
    book1 = Book("Head First Java", "George Orwell")
    book2 = Book("Clean Code", "Robert Martin")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Create User
    user = User("Emmanuel")

    print("\nAvailable books:")
    library.show_available_books()

    # Borrow a book
    print("\nBorrowing book...")
    user.borrow_book(book1)

    print("\nAvailable books after borrowing:")
    library.show_available_books()

    # Return book
    print("\nReturning book...")
    user.return_book(book1)

    print("\nAvailable books after returning:")
    library.show_available_books()

# This ensures the file runs only when executed directly
if __name__ == "__main__":
    main()



