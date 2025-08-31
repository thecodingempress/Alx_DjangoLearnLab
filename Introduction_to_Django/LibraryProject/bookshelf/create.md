from Book.models import Book
book = Book.Objects.create(
    title = '1984', 
    author = 'George Orwell', 
    publication_year = '1949')

#<QuerySet [<Book: Book object (1)>]>