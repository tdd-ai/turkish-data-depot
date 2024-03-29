from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.contrib import admin
from users.models import User


class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'is_staff')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff',)
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('password', 'email')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'affiliation')}),
        ('User Details', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'affiliation',
                       'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)