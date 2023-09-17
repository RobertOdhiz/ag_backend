from django.contrib import admin
from .models import FarmerProfile

class MyFarmerProfileAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name')
    search_fields = ('user__first_name', 'user__last_name')

    def user_first_name(self, obj):
        return obj.user.first_name
    
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.last_name
    
    user_last_name.short_description = 'Last Name'

admin.site.register(FarmerProfile, MyFarmerProfileAdmin)
