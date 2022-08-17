from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """ Changes the display in the admin page """
    list_display = ('blog_title', 'author', 'blog_body', 'date_created')


admin.site.register(Post, PostAdmin)