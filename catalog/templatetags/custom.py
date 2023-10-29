from django import template
from config import settings

register = template.Library()


# Тег для корректного вывода относительного пути к файлу
@register.simple_tag
def path_tag(format_string):
    return settings.MEDIA_URL + str(format_string)


# Фильтр для корректировки относительного пути к файлу
@register.filter
def path_filter(text):
    return settings.MEDIA_URL + str(text)


@register.simple_tag
def product_url(pk):
    return f"/product/{pk}"


@register.simple_tag
def post_url(pk):
    return f"/view/{pk}"


@register.simple_tag
def post_update(pk):
    return f"/post_update/{pk}"


@register.simple_tag
def product_update(pk):
    return f"/update_product/{pk}"


@register.simple_tag
def version_update(pk):
    return f"/update_version/{pk}"


@register.simple_tag
def post_delete(pk):
    return f"/delete/{pk}"


@register.simple_tag
def product_delete(pk):
    return f"/delete_product/{pk}"


@register.simple_tag
def version_delete(pk):
    return f"/delete_version/{pk}"
