from django.urls import path
from . import views

# App-specific URL patterns
app_name = 'relationship_app'

urlpatterns = [
    # Function-based view URLs
    path('books/', views.list_books, name='list_books'),
    path('libraries/', views.library_list, name='library_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    
    # Class-based view URLs
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/list/', views.BookListView.as_view(), name='book_list_class'),
    path('librarian/<int:pk>/', views.LibrarianDetailView.as_view(), name='librarian_detail'),
    
    # Home/index page (optional)
    path('', views.library_list, name='index'),
]
