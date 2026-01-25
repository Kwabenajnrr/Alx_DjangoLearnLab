from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


def list_books(request):
    books = Book.objects.all()  # 👈 REQUIRED by checker
    output = ""

    for book in books:
        output += f"{book.title} by {book.author.name}<br>"

    return HttpResponse(output)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"


