from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book, Library, Author, Librarian

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books in the database.
    Returns a rendered template with all books and their authors.
    """
    books = Book.objects.select_related('author').all()
    
    # For simple text response (uncomment if needed):
    # book_list = []
    # for book in books:
    #     book_list.append(f"{book.title} by {book.author.name}")
    # return HttpResponse("\n".join(book_list), content_type="text/plain")
    
    # Render template with context
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    including all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        
        # Get all books in this library with their authors
        context['books'] = library.books.select_related('author').all()
        
        # Get librarian for this library (if exists)
        try:
            context['librarian'] = library.librarian
        except Librarian.DoesNotExist:
            context['librarian'] = None
            
        return context

# Additional function-based view for demonstration
def library_list(request):
    """
    Function-based view that lists all libraries.
    """
    libraries = Library.objects.all()
    context = {
        'libraries': libraries
    }
    return render(request, 'relationship_app/library_list.html', context)

# Additional class-based view - ListView for books
class BookListView(ListView):
    """
    Class-based ListView alternative for listing books.
    """
    model = Book
    template_name = 'relationship_app/book_list.html'
    context_object_name = 'books'
    paginate_by = 10  # Optional pagination
    
    def get_queryset(self):
        """
        Optimize query to include author information.
        """
        return Book.objects.select_related('author').all()

# Function-based view for author details
def author_detail(request, author_id):
    """
    Function-based view to display author details and their books.
    """
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'relationship_app/author_detail.html', context)

# Class-based view for librarian details
class LibrarianDetailView(DetailView):
    """
    Class-based view to display librarian details.
    """
    model = Librarian
    template_name = 'relationship_app/librarian_detail.html'
    context_object_name = 'librarian'
