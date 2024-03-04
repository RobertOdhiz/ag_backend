from django.contrib import admin
from .models import FeedBack

class FeedBackAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'created_at', 'email', 'text')


admin.site.register(FeedBack, FeedBackAdminConfig)