from django.contrib import admin
from .models import Ghala, Rating

class GhalaAdmin(admin.ModelAdmin):
    list_display = ('ghala_name', 'phone_number', 'address', 'email', 'capacity')
    search_fields = ('ghala_name', 'phone_number', 'email')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('ghala_id', 'user_id', 'rating')
    list_filter = ('ghala_id', 'user_id')



admin.site.register(Ghala, GhalaAdmin)
admin.site.register(Rating, RatingAdmin)

