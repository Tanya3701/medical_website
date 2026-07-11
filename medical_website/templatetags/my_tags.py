from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/medical_website/images/{path}"
    else:
        return "#"
