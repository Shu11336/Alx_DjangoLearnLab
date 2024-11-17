from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"  # Replace with the actual author's name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = "Library Name"  # Replace with the actual library's name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")