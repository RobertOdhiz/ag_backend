from django.contrib import admin
from .models import MySoko

class MySokoAdmin(admin.ModelAdmin):
    list_display = ('user', 'commodity_sold', 'bags_sold', 'date_sold')
    search_fields = ('commodity_sold', 'user', 'bags_sold', 'date_sold')

admin.site.register(MySoko, MySokoAdmin)
