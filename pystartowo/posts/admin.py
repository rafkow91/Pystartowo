from django.contrib import admin
from .models import Post, ToAdd


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'published', 'sponsored']
    search_fields = ['title', 'content']
    list_filter = ['published', 'sponsored']
    autocomplete_fields = ('tags',)


@admin.register(ToAdd)
class ToAddAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'realised']
    search_fields = ['title', 'content']
    autocomplete_fields = ('tags',)
