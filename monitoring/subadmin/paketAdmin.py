from django.contrib import admin

class PaketAdmin(admin.ModelAdmin):
    fields = (
        'nama_paket', 
        'nama_opd',
        'dana', 
        'pagu', 
        'tahun_anggaran', 
        'hps', 
        'metode_pengadaan',
        'jenis_pengadaan',
        'nama_pptk', 
        'hp_pptk',
        'persen_fisik',
        'persen_keuangan',
        )
    
    list_display = [
        'nama_paket',
        'nama_opd',
        'dana',
        'pagu',
        'tahun_anggaran',
        'hps',
        'metode_pengadaan',
        'jenis_pengadaan',
        'nama_pptk',
        'persen_fisik',
        'persen_keuangan',
    ]
    
    list_display_links=[
        'nama_paket',
    ]
    
    list_filter = [
        'nama_opd',
        'dana',
        'tahun_anggaran',
        'metode_pengadaan',
        'jenis_pengadaan',
    ]
    
    ordering = (
        'nama_paket',
        'nama_opd',
        'dana',
        'tahun_anggaran',
        'metode_pengadaan',
        'nama_pptk',
        )