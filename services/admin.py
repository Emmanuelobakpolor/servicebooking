from django.contrib import admin
from .models import ServiceProvider

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('provider_name', 'service', 'location', 'availability')
