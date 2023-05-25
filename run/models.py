from django.db import models
from django.urls import reverse


# Create your models here.
class Year(models.Model):
    title = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('year_detail', args=[str(self.id)])


class Month(models.Model):
    title = models.CharField(max_length=100)
    total = models.PositiveIntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
