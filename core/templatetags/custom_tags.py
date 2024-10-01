from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def greet_user(name):
    return f'Привет, {name}!'

@register.filter
def format_date(value, date_format="%d-%m-%Y"):
    return value.strftime(date_format) if isinstance(value, datetime) else value