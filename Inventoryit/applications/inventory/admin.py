from django.contrib import admin

from .models import Inventory

class InventoryAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'location',
        'direction',
        'hostname',
        'nuuma',
        'serial_number',
        'product_number',
        'mac_address',
        'mac_wifi',
        'manufacturer',
        'name',
        'model',    
    )

    search_fields=('nuuma','hostname',)
    list_filter=('nuuma','hostname','model',)

admin.site.register(Inventory,InventoryAdmin)
