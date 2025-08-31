from Book.models import Book
book = Book(title = '1984', author = 'George Orwell', publication_year = '1949')
#<QuerySet [<Book: Book object (1)>]>

Book.objects.all()

#<QuerySet [<Book: Book object (1)>]>

book.publication_year = "Nineteen Eighty-Four"
book.save()

#ValueError: Field 'publication_year' expected a number but got 'Nineteen Eighty-Four'.

book.delete()

#(1, {'bookshelf.Book': 1})

Book.objects.all()

#<QuerySet []>