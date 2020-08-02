from django import template
from random import randint

register = template.Library()

@register.simple_tag
def random_int(a, b):
	return randint(a, b)
