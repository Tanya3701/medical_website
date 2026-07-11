from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """Тэг для правильного пути от изображения к шаблону"""
    if path:
        return f"/media/medical_website/images/{path}"
    else:
        return "#"
