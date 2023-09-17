from django.contrib import admin
from .models import Soko

class MySokoAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'price')
    search_fields = ('commodity', 'price')

admin.site.register(Soko, MySokoAdmin)
