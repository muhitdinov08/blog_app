from django.contrib import admin

from blog.models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'password']
    search_fields = ['first_name', 'last_name', 'user_name']

    # list_filter = ['post_count']
    #


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_active']
    search_fields = ['title', 'content']
    list_filter = ['author', 'is_active']
    # date_hierarchy = ["published_at"]
