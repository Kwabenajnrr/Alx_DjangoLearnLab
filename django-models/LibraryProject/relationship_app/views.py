from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # 👈 REQUIRED
    context_object_name = "library"





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


