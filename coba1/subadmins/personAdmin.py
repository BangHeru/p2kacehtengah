from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 
        'last_name',
        )
    
    list_display = [
        'first_name', 
        'last_name',
    ]
    
    list_display_links=[
        'first_name', 
        'last_name',
    ]
    
    list_filter = [
        'first_name', 
        'last_name',
    ]
    
    # date_hierarchy = 'tanggal_monitoring'
    
    ordering = (
        'first_name', 
        'last_name',
        )
    
    # readonly_fields = ('image_tag','admin_photo')

# admin.site.register(MonitoringAdmin, Person)
