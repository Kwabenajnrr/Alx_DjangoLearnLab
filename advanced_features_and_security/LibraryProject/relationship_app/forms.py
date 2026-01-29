from django import forms
from .models import Book
from .forms import BookForm
from bookshelf.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
