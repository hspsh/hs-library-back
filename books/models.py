from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    allowed_to_lend = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, default=None, blank=True)

    def __str__(self):
        return self.title
