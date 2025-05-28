from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')