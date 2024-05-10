from django.db import models
from django.urls import reverse


class Year(models.Model):
    year = models.PositiveIntegerField(unique=True, verbose_name='Год')
    january = models.PositiveIntegerField(verbose_name='Январь', default=0)
    february = models.PositiveIntegerField(verbose_name='Февраль', default=0)
    march = models.PositiveIntegerField(verbose_name='Март', default=0)
    april = models.PositiveIntegerField(verbose_name='Апрель', default=0)
    may = models.PositiveIntegerField(verbose_name='Май', default=0)
    june = models.PositiveIntegerField(verbose_name='Июнь', default=0)
    july = models.PositiveIntegerField(verbose_name='Июль', default=0)
    august = models.PositiveIntegerField(verbose_name='Август', default=0)
    september = models.PositiveIntegerField(verbose_name='Сентябрь', default=0)
    october = models.PositiveIntegerField(verbose_name='Октябрь', default=0)
    november = models.PositiveIntegerField(verbose_name='Ноябрь', default=0)
    december = models.PositiveIntegerField(verbose_name='Декабрь', default=0)
    total = models.PositiveIntegerField(verbose_name='Общий километраж')

    def get_month(self):
        monthies = [self.january, self.february, self.march, self.april,
                    self.may, self.june, self.july, self.august,
                    self.september, self.october, self.november,
                    self.december]
        return monthies

    def __str__(self):
        return str(self.year)

    def get_absolute_url(self):
        return reverse('run_home')
