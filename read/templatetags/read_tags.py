from django import template


register = template.Library()


@register.simple_tag()
def count_by_lang(year):
    books = year.books.values('language')
    total = len(books)
    eng, rus = 0, 0
    for lang in books:
        if lang['language'] == 'eng':
            eng += 1
        else:
            rus += 1
    return {
        'total': total,
        'eng': eng,
        'rus': rus
    }
