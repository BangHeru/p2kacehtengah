from django.contrib import admin
import datetime
from .models import Monitoring, Opd, Paket
from .subadmin.monitoringAdmin import *
from .subadmin.opdAdmin import  *
from .subadmin.paketAdmin import *
    

admin.site.site_header = "Halaman Admin P2K Aceh Tengah"
admin.site.site_title = "Sistem Pelaporan Monitoring P2K Aceh Tengah"
admin.site.index_title = "Selamat Datang di Sistem Pelaporan Monitoring P2K Aceh Tengah"

admin.site.register(Opd, OpdAdmin)
admin.site.register(Paket, PaketAdmin)
admin.site.register(Monitoring, MonitoringAdmin)

