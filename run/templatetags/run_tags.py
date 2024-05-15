from django import template

from run.models import Year


register = template.Library()


@register.simple_tag()
def get_total(year: Year):
    return sum(year.get_month())


@register.simple_tag()
def get_monthies():
    monthlies = [
            'january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december',
        ]
    return monthlies
