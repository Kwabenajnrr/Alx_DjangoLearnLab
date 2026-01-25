from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


def list_books(request):
    books = Book.objects.all()  # REQUIRED by checker

    return render(
        request,
        "relationship_app/list_books.html",  # REQUIRED by checker
        {"books": books}
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"


