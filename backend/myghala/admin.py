from django.contrib import admin
from .models import MyGhala

class MyGhalaAdmin(admin.ModelAdmin):
    list_display = ('user', 'bags_sold', 'date_rented', 'duration_of_storage')
    search_fields = ('ghala', 'user', 'date_rented')

admin.site.register(MyGhala, MyGhalaAdmin)
