from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from .opdModels import *



def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
    
class Paket(models.Model):
    SUMBER_DANA = [
        ('APBK', 'APBK'),
        ('DOKA', 'DOKA'),
        ('DAK', 'DAK'),
        ('TP', 'TP'),
    ]
    
    METODE_PENGADAAN = [
        ('SW', 'Swakelola'),
        ('TU', 'Tender'),
        ('EP', 'E-Katalog'),
        ('PL', 'Pengadaan Langsung'),
        ('TL', 'Penunjukan Langsung'),
    ]
    
    JENIS_PENGADAAN = [
        ('BR', 'Barang'),
        ('JK', 'Jasa Konstruksi'),
        ('JS', 'Jasa Lainnya'),
        ('KS', 'Konsultansi'),
    ]

    nama_paket = models.CharField(max_length=255, default="Paket Pekerjaan", blank=False)
    nama_opd = models.ForeignKey(Opd, on_delete=models.CASCADE)
    dana = models.CharField(max_length=4, choices=SUMBER_DANA,  default='APBK')
    pagu = models.PositiveIntegerField(default=0)
    tahun_anggaran = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    hps = models.PositiveIntegerField(default=0)
    metode_pengadaan = models.CharField(max_length=2, choices=METODE_PENGADAAN,  default='TU')
    jenis_pengadaan = models.CharField(max_length=2, choices=JENIS_PENGADAAN,  default='JK')
    nama_pptk = models.CharField(max_length=255, default="Nama PPTK", blank=False)
    hp_pptk = models.CharField(max_length=255, default="Nomor HP PPTK", blank=True)
    persen_fisik = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    persen_keuangan = models.DecimalField(default=0, max_digits=5, decimal_places=2)


    def __str__(self):
        return "%s" % (self.nama_paket)
    
