from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    publisher = models.CharField(max_length=10)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id},{self.title},{self.publisher},{self.price}"
