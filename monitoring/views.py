from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

# from .models import Monitoring
from .submodels.monitoringModels import *
# from .forms import FormDokumentasi

from .subviews.monitoringViews import *


def home(request):
    dokumentasi = Monitoring.objects.all().filter(tampil=True).order_by('prioritas')
    # return render(request, 'monitoring/home.html', { 'dokumentasi': dokumentasi })
    return render(request, 'monitoring/image_slide.html', { 'dokumentasi': dokumentasi })


