from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    return value.replace('arg', '')


# register.filter('cut', cut)
#Add my_extras in html file to load the custom filters like this {% load my_extras %}