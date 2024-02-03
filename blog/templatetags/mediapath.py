from django import template

register = template.Library()


@register.filter
def my_teg(value):
    if value:
        return f"/media/{value}"
    return ""
