from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.generic.detail import DetailView
from .forms import BookForm


# =========================
# Role check helpers
# =========================
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# =========================
# Role-based views
# =========================
@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='login')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# =========================
# Authentication views
# =========================
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        messages.error(request, "Registration failed. Please fix the errors.")
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('home')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')


# =========================
# Book CRUD views (permissions)
# =========================
@permission_required('relationship_app.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'relationship_app/edit_book.html', {'form': form})


@permission_required('relationship_app.delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'relationship_app/delete_book.html', {'book': book})


# =========================
# Library & Book views (checker-required)
# =========================
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",
        {"books": books}
    )
