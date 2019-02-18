import datetime

from django import template

register = template.Library()


@register.filter
def lower(value):
    return value.lower()

@register.filter()
def get_gender(value):
    return {
        "man": "Мужской",
        "woman": "Женский",
    }[value]

@register.tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.filter()
def get_pin_like(value, arg):
    return value[arg]
