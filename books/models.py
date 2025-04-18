from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    publish_date = models.DateField(null=True, blank=True)
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name 

    

