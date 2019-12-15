from __future__ import unicode_literals
import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars 
from django.db.models.signals import *
from django.dispatch import receiver


# monitoring.tools.pathAndRename import *

from .paketModels import *
from ..tools.pathAndRename import *
from ..tools.imageResize import  *

# path_and_rename = PathAndRename(os.path.join(settings.MEDIA_ROOT, 'dokumentasi/'))
path_and_rename = PathAndRename('dokumentasi/')

class Monitoring(models.Model):
    nama_paket = models.ForeignKey(Paket, on_delete=models.CASCADE)
    catatan = models.TextField(blank=True)
    # foto = models.ImageField(upload_to='dokumentasi/')
    # foto1 = models.ImageField(upload_to=path_and_rename, default='-')
    foto1 = models.ImageField(upload_to=path_and_rename, default='-')

    foto2 = models.ImageField(upload_to=path_and_rename, default='-')
    foto3 = models.ImageField(upload_to=path_and_rename, default='-')
    foto4 = models.ImageField(upload_to=path_and_rename, default='-')
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    tanggal_monitoring = models.DateField()
    persen_fisik = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    persen_keuangan = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    tampil = models.BooleanField(default=True)
    prioritas = models.PositiveSmallIntegerField(default=99)
    nama_pptk = models.CharField(max_length=255, default="Nama PPTK", blank=False)

    def save(self):
        self.lebar = 900
        self.tinggi = 700
        resize1 = ImageResize(self.foto1, self.lebar, self.tinggi)
        resize2 = ImageResize(self.foto2, self.lebar, self.tinggi)
        resize3 = ImageResize(self.foto3, self.lebar, self.tinggi)
        resize4 = ImageResize(self.foto4, self.lebar, self.tinggi)
        
        self.foto1 = resize1.proses()
        self.foto2 = resize2.proses()
        self.foto3 = resize3.proses()
        self.foto4 = resize4.proses()

        super(Monitoring,self).save()
   
    
    
    
    def get_nama_opd(self):
        return Paket.nama_opd

    def get_sumber_dana(self):
        return self.nama_paket.dana
    
    @property
    def short_description(self):
        return truncatechars(self.keterangan, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.foto1.url))
    admin_photo.short_description = 'Photo'
    admin_photo.allow_tags = True
    
    def sumber_dana(self):
        return self.dana, " Tahun Anggaran ", self.tahun
    
    def url_foto1(self):
            # # returns a URL for either internal stored or external image url
            # if self.externalURL:
            #     return self.externalURL
            # else:
            #     # is this the best way to do this??
        return os.path.join('/',settings.MEDIA_URL, 'dokumentasi/',os.path.basename(str(self.foto1)))
    

    def url_foto2(self):
        return os.path.join('/',settings.MEDIA_URL, 'dokumentasi/',os.path.basename(str(self.foto2)))


    def url_foto3(self):
        return os.path.join('/',settings.MEDIA_URL, 'dokumentasi/',os.path.basename(str(self.foto3)))


    def url_foto4(self):
        return os.path.join('/',settings.MEDIA_URL, 'dokumentasi/',os.path.basename(str(self.foto4)))



    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="100" height="100"/>&nbsp;'.format(self.url_foto1()) +
                         '<img src="{}" width="100" height="100"/>&nbsp;'.format(self.url_foto2()) +
                         '<img src="{}" width="100" height="100"/>&nbsp;'.format(self.url_foto3()) +
                         '<img src="{}" width="100" height="100"/>'.format(self.url_foto4()))

def __unicode__(self):
        # add __str__() if using Python 3.x
        return self.keterangan
    


# ==== delete image file when database is removed
@receiver(models.signals.post_delete, sender=Monitoring)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.foto1:
        if os.path.isfile(instance.foto1.path):
            os.remove(instance.foto1.path)
    
    if instance.foto2:
        if os.path.isfile(instance.foto2.path):
            os.remove(instance.foto2.path)
    
    if instance.foto3:
        if os.path.isfile(instance.foto3.path):
            os.remove(instance.foto3.path)
    
    if instance.foto4:
        if os.path.isfile(instance.foto4.path):
            os.remove(instance.foto4.path)
            
            
            

@receiver(models.signals.pre_save, sender=Monitoring)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_foto1 = sender.objects.get(pk=instance.pk).foto1
    except sender.DoesNotExist:
        return False

    new_foto1 = instance.foto1
    if not old_foto1 == new_foto1:
        if os.path.isfile(old_foto1.path):
            os.remove(old_foto1.path)
    
    # try remove file 2     
    try:
        old_foto2 = sender.objects.get(pk=instance.pk).foto2
    except sender.DoesNotExist:
        return False

    new_foto2 = instance.foto2
    if not old_foto2 == new_foto2:
        if os.path.isfile(old_foto2.path):
            os.remove(old_foto2.path)
            
            
    # try remove file 3     
    try:
        old_foto3 = sender.objects.get(pk=instance.pk).foto3
    except sender.DoesNotExist:
        return False

    new_foto3 = instance.foto3
    if not old_foto3 == new_foto3:
        if os.path.isfile(old_foto3.path):
            os.remove(old_foto3.path)
            
            
    # try remove file 4     
    try:
        old_foto4 = sender.objects.get(pk=instance.pk).foto4
    except sender.DoesNotExist:
        return False

    new_foto4 = instance.foto4
    if not old_foto4 == new_foto4:
        if os.path.isfile(old_foto4.path):
            os.remove(old_foto4.path)
            
            

