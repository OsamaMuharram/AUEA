from django.conf import settings
from django.shortcuts import render
from.models import cabinet
from document.models import parent_document
import os



def index1(request):
    object_list = cabinet.objects.all()
    context = {'object_list': object_list}

    return render(request, 'cabinet/index.html', context)

def show_element(request,Management_name):
    #ارجhع قيم المستندات من خلال الفولدرات باستخدما مكتبة os
    """object_list_from_dir = cabinet.objects.filter(Management_name=Management_name)[0]
    path = settings.MEDIA_ROOT + object_list_from_dir.Mgment_path
    dir_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            dir_list.append(filename)"""

    #ارجاع كل المستندات الموجوده فى قاعدة البيانات الخاصة بالوثائق ووضعها تحت المجلد الخاص بها
    object_list_from_db=parent_document.objects.filter(select_cabinet__Management_name=Management_name)

    name = Management_name


    context = {'name':Management_name,
               'object_list_from_db':object_list_from_db}

    return render(request, 'cabinet/show_element.html', context)
