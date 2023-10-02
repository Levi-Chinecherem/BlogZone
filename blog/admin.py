# blog/admin.py

from django.contrib import admin
from .models import *

# Set custom headers and titles
admin.site.site_header = 'BlogZon Admin'
admin.site.site_title = 'Administration!'
admin.site.index_title = 'BlogZone'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'author', 'get_likes_count', 'get_favorites_count', 'timestamp')
    search_fields = ('title', 'author__username')
    list_filter = ('title', 'category', 'author', )

    def get_likes_count(self, obj):
        return obj.likes.count()

    get_likes_count.admin_order_field = 'likes__count'
    get_likes_count.short_description = 'Likes Count'

    def get_favorites_count(self, obj):
        return obj.favorites.count()

    get_favorites_count.admin_order_field = 'favorites__count'
    get_favorites_count.short_description = 'Favorites Count'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'timestamp')
    search_fields = ('author__username', 'post__title')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)