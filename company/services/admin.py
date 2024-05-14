from django.contrib import admin
from .models import ServiceCategory, Service

# Register your models here.

class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
