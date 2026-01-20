import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        
        print(f"\n=== Books by {author_name} ===")
        for book in books:
            print(f"- {book.title}")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"\n=== Books in {library_name} ===")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        
        print(f"\n=== Librarian for {library_name} ===")
        print(f"Librarian: {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


if __name__ == "__main__":
    print("Django ORM Relationship Queries")
    print("=" * 50)
    
    # Add sample data first (run this once)
    # Then comment it out and run the queries
    
    # Uncomment below to create sample data:
    """
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter", author=author)
    library = Library.objects.create(name="Central Library")
    library.books.add(book1)
    librarian = Librarian.objects.create(name="Alice Johnson", library=library)
    print("Sample data created!")
    """
    
    # Run queries:
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")