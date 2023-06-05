from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Year(models.Model):
    title = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='1')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('run_home')


class Month(models.Model):
    title = models.CharField(max_length=100)
    total = models.PositiveIntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='monthes')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('run_home')
