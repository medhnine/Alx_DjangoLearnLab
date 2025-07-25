from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.list_books, name='book'),
    path('library/<int:pk>/', views.ViewLibrary.as_view(), name='view_library'),
    
    # Auth
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', views.register_user, name='register'),  # ✅ function-based register view
    
    # Dashboards
    path('admin-only/', views.admin_dashboard, name='admin_view'),
    path('librarian/', views.librarian_dashboard, name='librarian_view'),
    path('member/', views.membership_dashboard, name='member_view'),

    # Book actions
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
