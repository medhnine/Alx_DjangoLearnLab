import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ----------- Query 1: Query all books by a specific author -----------
author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f" - {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' does not exist.")

# ----------- Query 2: List all books in a library -----------
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(f" - {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' does not exist.")

# ----------- Query 3: Retrieve the librarian for a library -----------
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' does not exist.")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}.")

