from django.contrib import admin
from .models import Book

admin.site.register(Book)
# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "publication_year") #columns to display in teh Admin list view
    list_filter = ("Author") #Filters on the right hand side
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)