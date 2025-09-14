from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(null=True, blank=True)  # used by template
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    class Meta:
        # NOTE: Django already provides add/change/delete permissions, but the task
        # explicitly asks for custom ones too.
        permissions = (
            ('can_add_book', 'Can add book (custom)'),
            ('can_change_book', 'Can change book (custom)'),
            ('can_delete_book', 'Can delete book (custom)'),
        )

    def __str__(self):
        return f"{self.title} ({self.author})"


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, related_name='librarian', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} @ {self.library}"


# ---------- Roles ----------
class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"