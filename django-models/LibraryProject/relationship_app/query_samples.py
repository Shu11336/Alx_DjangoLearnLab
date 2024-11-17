# samples.py

import os
import django

# Initialize Django settings (adjust 'your_project.settings' to your actual project settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from library_app.models import Library, Book, Author, Librarian  # Adjust the import path based on your app name


def get_library_books(library_name):
    """Fetch all books in a specified library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in the '{library_name}' library:")
        for book in books:
            print(f"- {book.name} (Author: {book.author.name})")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")


def get_author_books(author_name):
    """Fetch all books written by a specified author using related_name."""
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books written by '{author_name}':")
        for book in books:
            print(f"- {book.name}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")


def get_books_by_author_filter(author_name):
    """Fetch all books by an author using objects.filter()."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by '{author_name}' (using filter):")
        for book in books:
            print(f"- {book.name}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")


def get_libraries_with_book(book_name):
    """Fetch all libraries that have a specified book."""
    try:
        book = Book.objects.get(name=book_name)
        libraries = book.libraries.all()
        print(f"Libraries that have the book '{book_name}':")
        for library in libraries:
            print(f"- {library.name}")
    except Book.DoesNotExist:
        print(f"Book '{book_name}' does not exist.")


def get_librarian_by_library(library_name):
    """Fetch the librarian responsible for a specified library using Librarian.objects.get()."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian of '{library_name}' library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the '{library_name}' library.")


if __name__ == '__main__':
    # Sample usage
    get_library_books("Central Library")
    print("\n" + "="*50 + "\n")
    
    get_author_books("J.K. Rowling")
    print("\n" + "="*50 + "\n")
    
    get_books_by_author_filter("J.K. Rowling")
    print("\n" + "="*50 + "\n")
    
    get_libraries_with_book("Harry Potter")
    print("\n" + "="*50 + "\n")
    
    get_librarian_by_library("Central Library")
