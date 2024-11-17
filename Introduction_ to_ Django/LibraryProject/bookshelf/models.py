from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = Book.objects.aggregate(models.Max('id'))['id__max']
            self.id = max_id + 1 if max_id else 1
        super(Book, self).save(*args, **kwargs)


    def __str__(self):
        return f"id={self.id} title= {self.title} author= {self.author} published in the year {self.publication_year}"