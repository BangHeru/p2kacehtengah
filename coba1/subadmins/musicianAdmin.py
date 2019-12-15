from django.contrib import admin

class MusicianAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 
        'last_name',
        'instrument',
        )
    
    list_display = [
        'first_name', 
        'last_name',
        'instrument',
    ]
    
    list_display_links=[
        'first_name', 
        'last_name',
    ]
    
    list_filter = [
        'first_name', 
        'last_name',
        'instrument',
    ]
    
    # date_hierarchy = 'release_date'
    
    ordering = (
        'first_name', 
        'last_name',
        'instrument',
        )
    
    # readonly_fields = ('image_tag','admin_photo')
