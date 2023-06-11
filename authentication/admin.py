from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'date_joined', 'is_admin', 'is_staff', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None)
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active'),
        }),
    )
    ordering = ()


admin.site.register(CustomUser, UserAdmin)
