from bookstore.models import Book

book.publication_year = "Nineteen Eighty-Four"
book.save()

#ValueError: Field 'publication_year' expected a number but got 'Nineteen Eighty-Four'.