# Explaining Each View 

#Added django-filter in INSTALLED APPS
#added needed settings for the filter to work

#REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

class BookListView(generics.ListAPIView):
    """
        Provides a read-only list of all books.
        * Only authenticated users are allowed to access this view or they will be allowed to READ it only.
        * Supports basic filtering based on title, publication year, and author.
        *Installed django-filter with pip install django-filter
        *added it in INSTALLED APPS and added the settings needed
        *imported DjangoFilterBackend
        *and added the fields i want to filter
    """

class BookDetailView(generics.RetrieveAPIView):
    """
        Provides a read-only list of a single book.
        * Only authenticated users are allowed to access this view or they will be allowed to READ it only.
    """

class BookCreateView(generics.CreateAPIView):
    """
        Provides a create API point for the Book.
        * Only authenticated users are allowed to access this view.
    """

class BookUpdateView(generics.UpdateAPIView):
    """
        Provides a Update API point for a single Book.
        * Only authenticated users are allowed to access this view.
    """

class BookDeleteView(generics.DestroyAPIView):
    """
        Provides a Delete API point for the Book.
        * Only authenticated users are allowed to access this view.
    """