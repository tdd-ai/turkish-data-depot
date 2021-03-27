from django.contrib import admin
from .models import *

class DatasetAdmin(admin.ModelAdmin):
    model = Dataset
    list_display = ('catalog', 'is_visible', 'type', 'name')

admin.site.register(Type)
admin.site.register(DataType)
admin.site.register(Annotation)
admin.site.register(Source)
admin.site.register(Compression)
admin.site.register(License)

admin.site.register(Dataset, DatasetAdmin)