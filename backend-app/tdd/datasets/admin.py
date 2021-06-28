from django.contrib import admin
from .models import *

class DatasetAdmin(admin.ModelAdmin):
    model = Dataset
    list_display = ('name', 'catalog', 'is_visible', 'type', 'name')
    exclude = ('id', 'serial_number')
    readonly_fields = ('catalog',)

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

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if FileItem.objects.filter(dataset_id=object_id).count():
            self.change_form_template = "admin/dataset_file_uploaded_form.html"
        else:
            self.change_form_template = 'admin/dataset_change_form.html'
        return self.changeform_view(request, object_id, form_url, extra_context)

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


class CatalogEnumAdmin(admin.ModelAdmin):
    model = CatalogEnum
    list_display = ('name', 'description', 'catalog_acronym')

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


class FileItemAdmin(admin.ModelAdmin):
    model = FileItem
    list_display = ('dataset',)


admin.site.register(Type, CatalogEnumAdmin)
admin.site.register(DataType, EnumAdmin)
admin.site.register(Annotation, EnumAdmin)
admin.site.register(Source, EnumAdmin)
admin.site.register(Format, EnumAdmin)
admin.site.register(Compression, EnumAdmin)
admin.site.register(License, CatalogEnumAdmin)

admin.site.register(Dataset, DatasetAdmin)
admin.site.register(FileItem, FileItemAdmin)