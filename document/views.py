import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from cabinet.models import cabinet

def index(request):

    return render(request, 'document/index.html', {'':''})


def display_document(request):
    path = settings.MEDIA_ROOT
    files_list_0 = os.listdir(path)
    context = {'files': files_list_0}
    return render(request, "document/display.html", context)

def display_selected_document(request,file):
    #استدعاء المسار الخاص بالادارة من قاعدة البيانات
    correct_path=cabinet.objects.filter(Management_name=file)[0].Mgment_path

    path=settings.MEDIA_ROOT+correct_path
    files_list_1 = os.listdir(path)


    context = {'files': files_list_1}
    return render(request, "document/display_selected_document.html", context)