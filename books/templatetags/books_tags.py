from django import template

register = template.Library()

@register.filter
def to_lowercase(value , args):
    return f'{args} :{value.lower()}'
