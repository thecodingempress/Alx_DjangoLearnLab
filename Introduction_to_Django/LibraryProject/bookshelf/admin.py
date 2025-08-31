from django.contrib import admin
from bookshelf.models import Book

admin.site.register(Book)
# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display = ("author", "title", "publication_year") #columns to display in teh Admin list view
    list_filter = ("Author") #Filters on the right hand side


admin.site.register(Book, BookAdmin)