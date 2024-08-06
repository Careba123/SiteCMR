import os
from django import template

register = template.Library()

@register.filter
def basename(value):
    print("basename filter is called")
    return os.path.basename(value)
