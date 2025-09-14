from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']  # add other fields as needed
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, label="Title")