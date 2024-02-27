from django import template

register = template.Library()

@register.filter
def crop_string(value):
    if len(value) > 15:
        return value[:12] + '...'
    else:
        return value

@register.filter
def split(value, delimiter):
    return value.split(delimiter)

@register.filter
def checkURL(value):
    if hasattr(value, 'ingo_text'):
        return '/articles'
    elif hasattr(value, 'file_list'):
        return '/files'
    else:
        return '/employes'