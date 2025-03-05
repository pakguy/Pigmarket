from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(Breeds)
admin.site.register(Sex)
admin.site.register(TagsColour)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('email', 'username', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)