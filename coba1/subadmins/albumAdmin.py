from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    fields = (
        'artist', 
        'name',
        'release_date',
        'num_stars',
        )
    
    list_display = [
        'artist', 
        'name',
        'release_date',
        'num_stars',
    ]
    
    list_display_links=[
        'artist', 
        'name',
    ]
    
    list_filter = [
        'artist', 
        'name',
        'release_date',
        'num_stars',
    ]
    
    date_hierarchy = 'release_date'
    
    ordering = (
        'artist', 
        'name',
        'release_date',
        'num_stars',
        )
    
    # readonly_fields = ('image_tag','admin_photo')
