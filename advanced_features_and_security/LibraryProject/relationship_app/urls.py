from django.urls import path
from .views import (
    list_books, LibraryDetailView,
    AppLoginView, AppLogoutView, register,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # books / libraries
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # auth
    path('login/', AppLoginView.as_view(), name='login'),
    path('logout/', AppLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # role-based
    path('admin-only/', admin_view, name='admin_only'),
    path('librarian-only/', librarian_view, name='librarian_only'),
    path('member-only/', member_view, name='member_only'),

    # secured CRUD for books
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
