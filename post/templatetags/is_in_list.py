from django import template
register = template.Library()


# 判断value是否在llist中
@register.filter
def is_in_list(value, llist):
    return (str(value) in llist)
