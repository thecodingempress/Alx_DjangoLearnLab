# LibraryProject/relationship_app/query_samples.py
from .models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Return a queryset of all books written by the given author name.
    """
    return Book.objects.filter(author__name=author_name)

def list_books_in_library(library_name):
    """
    Return a queryset of all books available in the specified library.
    """
    library = Library.objects.get(name=library_name)  # <-- required exact string
    return library.books.all()

def get_librarian_for_library(library_name):
    """
    Return the Librarian instance for the specified library.
    """
    library = Library.objects.get(name=library_name)  # <-- required exact string
    return library.librarian
