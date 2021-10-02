from django import template

register = template.Library()


@register.simple_tag
def my_range(num):
    return range(int(num))
