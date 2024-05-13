from django.db import models
from django.urls import reverse


class Year(models.Model):
    title = models.PositiveIntegerField(unique=True, verbose_name='Год')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('read_app:read_home')


class Book(models.Model):
    LANG = (
        ('rus', 'Русский'),
        ('eng', 'Английский'),
    )

    title = models.CharField(unique=True,
                             verbose_name='Название', max_length=140)

    author = models.CharField(max_length=140, verbose_name='Автор')

    year = models.ForeignKey(Year, related_name='books',
                             on_delete=models.CASCADE,
                             verbose_name='Год прочтения')

    language = models.CharField(max_length=3, choices=LANG,
                                verbose_name='Язык')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read_app:read_home')
