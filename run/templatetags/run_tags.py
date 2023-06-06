from django import template
from django.db.models import Sum

register = template.Library()


@register.simple_tag()
def get_total(year):
    summ = year.monthes.aggregate(Sum('total'))
    return summ['total__sum']
