# views.py

from django.shortcuts import render, get_object_or_404
from .models import Library  # Ensure this import is present

def library_detail(request, library_id):
    """View to display details of a specific library."""
    # Fetch the library object using get_object_or_404 for error handling
    library = get_object_or_404(Library, id=library_id)
    
    # Render the 'relationship_app/library_detail.html' template with the library context
    return render(request, 'relationship_app/library_detail.html', {'library': library})
