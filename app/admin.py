from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserRegistrar, SocietyModel

class CustomUserAdmin(UserAdmin):

    model = CustomUser

    list_display = ('email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('email', 'password', )
            }),
        (('Personal_info'), {
          'classes': ['wide'],
          'fields': ('first_name', 'last_name')
            }),
        ('Permissions', {
            'classes': ['wide'],
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
            }),
        ('Dates', {
            'classes': ['wide'],
            'fields': ('last_login', 'date_joined')
            })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserRegistrar)
class UserRegistrarAdmin(admin.ModelAdmin):
    list_display = ["email", "firstName", "lastName", "level"]
    search_fields = ["email", "level", "societies"]
    list_filter = ["email", "level", "societies"]
    ordering = ["email"]
    
@admin.register(SocietyModel)
class SocietyModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created"]
    search_fields = ["name"]
    