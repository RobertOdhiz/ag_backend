from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff',
                    'is_active', 'is_superuser', 'is_farmer')
    ordering = ('-created_at',)
    list_display = ('email', 'first_name', 'last_name',
                    'is_farmer', 'is_active', 'is_staff',
                    )

    fieldsets = (
        ('Personal', {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_farmer', 'is_superuser', 'is_active')}),
        ('More Details', {'fields': ('create_at', 'updated_at', 'last_login')}),
    )

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2', 'is_active', 'is_farmer', 'is_staff'),
    }),
)



admin.site.register(NewUser, UserAdminConfig)
