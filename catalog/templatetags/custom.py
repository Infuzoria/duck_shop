from django import template
from config import settings
from django.db import connection

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


@register.simple_tag
def get_user_group(user_id):
    with connection.cursor() as crs:
        crs.execute("select auth_group.name from users_user left join users_user_groups on "
                    "users_user.id = users_user_groups.user_id left join auth_group on "
                    "users_user_groups.group_id = auth_group.id where users_user.id = %s;", [user_id])
        rows = crs.fetchone()

    if rows[0]:
        return rows[0]
    return ''
