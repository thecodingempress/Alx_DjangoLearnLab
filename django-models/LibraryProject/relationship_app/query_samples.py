"""
Run with either:
    python manage.py shell -c "import relationship_app.query_samples as qs; qs.run()"
or (replace 'practice_project' with your project name):
    DJANGO_SETTINGS_MODULE=practice_project.settings python relationship_app/query_samples.py
"""
import os
import django

def _setup():
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        # adjust if your settings module is named differently
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')
    django.setup()

def books_by_author(author_name):
    from relationship_app.models import Book
    return list(Book.objects.select_related('author')
                .filter(author__name__iexact=author_name)
                .values_list('title', flat=True))

def books_in_library(library_name):
    from relationship_app.models import Library
    lib = Library.objects.prefetch_related('books__author').get(name__iexact=library_name)
    return [f"{b.title} by {b.author.name}" for b in lib.books.all()]

def librarian_for_library(library_name):
    from relationship_app.models import Library
    lib = Library.objects.select_related('librarian').get(name__iexact=library_name)
    return getattr(lib.librarian, 'name', None)

def run():
    _setup()
    print("Books by 'Jane Doe':", books_by_author('Jane Doe'))
    print("Books in 'Central Library':", books_in_library('Central Library'))
    print("Librarian for 'Central Library':", librarian_for_library('Central Library'))

if __name__ == '__main__':
    _setup()
    print(run())