# blog/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='has_liked')
def has_liked(post, user):
    return post.likes.filter(id=user.id).exists()

@register.filter(name='has_favorited')
def has_favorited(post, user):
    return post.favorites.filter(id=user.id).exists()
