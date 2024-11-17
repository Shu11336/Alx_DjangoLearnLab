from rest_framework import serializers
from .models import Book
from .models import Author
from django.utils import timezone


# BookSerializer to handle the Book Model with custom validation to publication year , i import timezone to get the correct
# date then compared it and either returned the value of the publication_year or raised an error if its wrong
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value):
        now = timezone.now().year
        if value > now:
            raise serializers.ValidationError("Publication Year can't be in the Future")
        return value


# AuthorSerializer to handle Author Model , we add nested BookSerializer so it dynamically chooses the books related to
# that author , with many=True so there might be many books and its nested , and read_only=True so you can't edit it
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
