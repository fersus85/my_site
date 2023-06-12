from django import template
from django.db.models import Sum, Count

register = template.Library()


@register.simple_tag()
def get_eng(year):
    summ = year.books.filter(language='eng').aggregate(Count('title'))
    return summ['title__count']


@register.simple_tag()
def get_rus(year):
    summ = year.books.filter(language='rus').aggregate(Count('title'))
    return summ['title__count']
