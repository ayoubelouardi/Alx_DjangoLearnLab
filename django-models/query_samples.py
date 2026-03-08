import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "LibraryProject"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def list_all_books_in_library(library_name):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian


if __name__ == "__main__":
    print("Sample Queries for Django Model Relationships")
    print("=" * 50)
