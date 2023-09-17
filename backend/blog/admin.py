from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'reads', 'date_posted')
    search_fields = ('author', 'reads', 'date_posted')

admin.site.register(Blog, BlogAdmin)