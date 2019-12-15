from django.db import models

class Opd(models.Model):
    nama_opd = models.CharField(max_length=255, default="OPD", blank=False)
    kepala_opd = models.CharField(max_length=255, default="Nama Kepala OPD", blank=False)
    alamat_opd = models.TextField(blank=True)
    bendahara_opd = models.CharField(max_length=255, default="Nama Bendahara OPD", blank=False)
    
    def __str__(self):
        return "%s" % (self.nama_opd)
    
