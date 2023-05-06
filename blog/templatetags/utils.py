from django import template
import math

register = template.Library()


eq = dict(zip('əüöğçşıƏÜÖĞÇŞ', 'euogcsiEUOGCS'))
@register.filter
def convert_en(text):
    result = ''
    for l in text:
        result += eq.get(l, l)
    return result


@register.simple_tag
def edit_params(request, key, value):
    params = request.GET.copy()
    params[key] = value
    return '?' + params.urlencode()


@register.inclusion_tag('includes/stars.html')
def create_stars(value):
    print('salam')
    if not value:
        return {'no_review': True}

    filled_stars = math.floor(value)
    half_stars = math.ceil(value - filled_stars)
    empty_stars = 5 - (filled_stars + half_stars)
    return {'filled_stars': range(filled_stars),
            'half_stars': half_stars, 
            'empty_stars': range(empty_stars)}