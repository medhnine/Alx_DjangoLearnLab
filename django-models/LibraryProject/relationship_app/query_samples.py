#!/usr/bin/env python
"""
Sample queries demonstrating Django ORM relationships.
Run this script from the Django project root with:
python manage.py shell < relationship_app/query_samples.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for testing queries."""
    print("Creating sample data...")
    
    # Create Authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="Agatha Christie")
    
    # Create Books
    book1, created = Book.objects.get_or_create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3, created = Book.objects.get_or_create(title="1984", author=author2)
    book4, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    book5, created = Book.objects.get_or_create(title="Murder on the Orient Express", author=author3)
    
    # Create Libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="University Library")
    
    # Add books to libraries (ManyToMany relationships)
    library1.books.add(book1, book2, book3, book5)
    library2.books.add(book2, book3, book4, book5)
    
    # Create Librarians
    librarian1, created = Librarian.objects.get_or_create(name="Alice Johnson", library=library1)
    librarian2, created = Librarian.objects.get_or_create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!\n")

def query_books_by_author():
    """Query all books by a specific author (ForeignKey relationship)."""
    print("=" * 50)
    print("QUERY 1: Books by a specific author")
    print("=" * 50)
    
    # Method 1: Using filter on Book model with author object
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author.name} (using Book.objects.filter(author=author)):")
        for book in books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print("Author 'J.K. Rowling' not found.")
    
    # Method 2: Using filter with author name lookup
    author_name = "J.K. Rowling"
    books = Book.objects.filter(author__name=author_name)
    
    print(f"\nBooks by {author_name} (using Book.objects.filter(author__name)):")
    for book in books:
        print(f"  - {book.title}")
    
    # Method 3: Using reverse relationship from Author
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        
        print(f"\nBooks by {author_name} (using reverse relationship):")
        for book in books_by_author:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    
    print("\n")

def query_books_in_library():
    """List all books in a library (ManyToMany relationship)."""
    print("=" * 50)
    print("QUERY 2: Books in a specific library")
    print("=" * 50)
    
    library_name = "Central Library"
    
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        # Alternative: Query from Book side
        print(f"\nAlternative query - Books available at {library_name}:")
        books_alt = Book.objects.filter(libraries__name=library_name)
        for book in books_alt:
            print(f"  - {book.title} by {book.author.name}")
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    
    print("\n")

def query_librarian_for_library():
    """Retrieve the librarian for a library (OneToOne relationship)."""
    print("=" * 50)
    print("QUERY 3: Librarian for a specific library")
    print("=" * 50)
    
    library_name = "Central Library"
    
    try:
        library = Library.objects.get(name=library_name)
        
        # Method 1: Using the reverse OneToOne relationship
        try:
            librarian = library.librarian
            print(f"Librarian at {library_name}: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"No librarian assigned to {library_name}")
        
        # Method 2: Using get() on Librarian model
        try:
            librarian_alt = Librarian.objects.get(library=library)
            print(f"Librarian (alternative query): {librarian_alt.name}")
        except Librarian.DoesNotExist:
            print(f"No librarian found for {library_name}")
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    
    print("\n")

def additional_relationship_queries():
    """Additional queries demonstrating complex relationships."""
    print("=" * 50)
    print("ADDITIONAL QUERIES: Complex relationship examples")
    print("=" * 50)
    
    # Query 1: Find all libraries that have books by a specific author
    print("Libraries with books by George Orwell:")
    libraries_with_orwell = Library.objects.filter(books__author__name="George Orwell").distinct()
    for library in libraries_with_orwell:
        print(f"  - {library.name}")
    
    # Query 2: Count books per library
    print("\nBook count per library:")
    libraries = Library.objects.all()
    for library in libraries:
        book_count = library.books.count()
        print(f"  - {library.name}: {book_count} books")
    
    # Query 3: Find authors whose books are in multiple libraries
    print("\nAuthors with books in multiple libraries:")
    authors = Author.objects.filter(books__libraries__isnull=False).annotate(
        library_count=models.Count('books__libraries', distinct=True)
    ).filter(library_count__gt=1)
    
    for author in authors:
        print(f"  - {author.name}")
    
    print("\n")

if __name__ == "__main__":
    print("Django Model Relationships - Query Samples")
    print("=========================================\n")
    
    # Create sample data first
    create_sample_data()
    
    # Run the required queries
    query_books_by_author()
    query_books_in_library()
    query_librarian_for_library()
    
    # Run additional queries for learning
    additional_relationship_queries()
    
    print("Query samples completed!")
