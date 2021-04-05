from django.contrib import admin
from .models import *

class DatasetAdmin(admin.ModelAdmin):
    model = Dataset
    list_display = ('catalog', 'is_visible', 'type', 'name')
    exclude = ('id',)

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_module_permission(self, request):
        return True

class EnumAdmin(admin.ModelAdmin):
    model = Enum
    list_display = ('name', 'description')

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_module_permission(self, request):
        return True

admin.site.register(Type, EnumAdmin)
admin.site.register(DataType, EnumAdmin)
admin.site.register(Annotation, EnumAdmin)
admin.site.register(Source, EnumAdmin)
admin.site.register(Format, EnumAdmin)
admin.site.register(Compression, EnumAdmin)
admin.site.register(License, EnumAdmin)

admin.site.register(Dataset, DatasetAdmin)