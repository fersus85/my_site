from django import template
from django.db.models import Count
from read.models import Book
register = template.Library()


@register.simple_tag()
def get_books_total():
    summ = Book.objects.all().aggregate(Count('title'))
    return summ['title__count']
