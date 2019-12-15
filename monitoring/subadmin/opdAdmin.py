from django.contrib import admin

class OpdAdmin(admin.ModelAdmin):
    #actions_selection_counter = True
    #actions_on_bottom = False
    #actions_on_top = True
    fields = (
        'nama_opd', 
        'kepala_opd',
        'bendahara_opd', 
        'alamat_opd'
        )
    
    list_display = [
        'nama_opd',
        'kepala_opd',
        'bendahara_opd',
        'alamat_opd',
    ]
    
    list_display_links=[
        'nama_opd',
    ]
    
    list_filter = [
        'nama_opd',
        'kepala_opd',
    ]
    
    ordering = ("nama_opd",)
    

