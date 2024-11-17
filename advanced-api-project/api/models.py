from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        app_label = 'api'

# Book Model with a Foregin key relationship with author , stating that one author can have many books ,
# with related_name related_name = books so we can use it in the serializer and on_delete = Cascade so if we delete
# the author we delete the books related to it as well

class Book(models.Model):
    title = models.CharField(max_length=180)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
