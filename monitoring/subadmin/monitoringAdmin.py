from django.contrib import admin
    
class MonitoringAdmin(admin.ModelAdmin):
    fields = (
        'nama_paket', 
        'image_tag',
        'foto1', 
        'foto2', 
        'foto3', 
        'foto4', 
        'catatan',
        'tanggal_monitoring',
        'persen_fisik',
        'persen_keuangan',
        'nama_pptk',
        'tampil', 
        'prioritas',
        )
    
    list_display = [
        'admin_photo',
        'nama_paket',
        'catatan',
        'tanggal_monitoring',
        'persen_fisik',
        'persen_keuangan',
        'nama_pptk',
        'tampil',
        'prioritas',
    ]
    
    list_display_links=[
        'admin_photo',
        'nama_paket',
    ]
    
    list_filter = [
        'prioritas',
        'tampil',
        'nama_paket', 

    ]
    
    # search_fields = [
    #     'Paket__nama_paket', 
    #     # 'nama_pptk',
    # ]
    
    date_hierarchy = 'tanggal_monitoring'
    
    ordering = (
        'prioritas',
        'persen_fisik',
        'persen_keuangan',
        'nama_pptk',
        'tanggal_monitoring',
        )
    
    readonly_fields = ('image_tag','admin_photo')



