from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django import forms

from .models import Book, Library

# --------- Function-based view: list all books ----------
@login_required
def list_books(request):
    # Must use Book.objects.all()
    books = Book.objects.all()
    # Return simple text, not a template
    lines = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")


# --------- Class-based view: library detail ----------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --------- Auth views ----------
class AppLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class AppLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # profile is auto-created by signal
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --------- Role helpers & role-restricted views ----------
def _has_role(user, role):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == role

def is_admin(user): return _has_role(user, 'Admin')
def is_librarian(user): return _has_role(user, 'Librarian')
def is_member(user): return _has_role(user, 'Member')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --------- Book CRUD with custom permissions ----------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
