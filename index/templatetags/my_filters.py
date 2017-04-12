from django import template
register = template.Library()

# @register.filter(name = 'get_class')

@register.filter(name='dir')
def fun04121239(obj):
    return dir(obj)


@register.filter(name='type')
def fun04121240(obj):
    return type(obj)

@register.filter(name='str')
def fun04121241(obj):
    return str(obj)

@register.filter(name='verbose')
def fun04121241(obj):
    return ""


# add tag class
@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})