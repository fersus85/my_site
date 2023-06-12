from django.db import models
from django.urls import reverse


# Create your models here.

class Year(models.Model):
    title = models.PositiveIntegerField()

    def __str__(self):
        t = str(self.title)
        return t

    def get_absolute_url(self):
        return reverse('read_home')


class Book(models.Model):
    choices = (
        ('rus', 'rus'),
        ('eng', 'eng'),
    )
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    year = models.ForeignKey(Year, related_name='books', on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read_home')
