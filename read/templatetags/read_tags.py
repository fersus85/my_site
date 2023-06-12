from django import template
from django.db.models import Sum, Count
from django.core.cache import cache
register = template.Library()


@register.simple_tag()
def get_eng(year):
    summ = cache.get('sum')
    if not summ:
        summ = year.books.filter(language='eng').aggregate(Count('title'))
        cache.set('sum', summ, 120)
    return summ['title__count']


@register.simple_tag()
def get_rus(year):
    summ = year.books.filter(language='rus').aggregate(Count('title'))
    return summ['title__count']
