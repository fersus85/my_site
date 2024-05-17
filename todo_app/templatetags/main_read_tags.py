from django import template
from django.db.models import Count
from django.core.cache import cache

from read.models import Book


register = template.Library()


@register.simple_tag()
def get_books_total():
    total_books = cache.get('total')
    if not total_books:
        total_books = Book.objects.all().aggregate(Count('title'))
        cache.set('total', total_books, 40)
    return total_books['title__count']
