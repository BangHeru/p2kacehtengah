from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers import serialize

from ..submodels.monitoringModels import *




def laporan(request):
    dokumentasi = Monitoring.objects.all().filter(tampil=True)
    hsl = serialize('json', dokumentasi, cls=LazyEncoder)
    return JsonResponse(hsl,  safe=False)
    # qs_json = serializers.serialize('json', dokumentasi)
    # return HttpResponse(qs_json, content_type='application/json')

def test_ping(request):
    return HttpResponse('got ping')
