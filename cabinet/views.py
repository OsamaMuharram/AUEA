from django.conf import settings
from django.shortcuts import render
from.models import cabinet
import os



def index1(request):
    object_list = cabinet.objects.all()
    context = {'object_list': object_list}
    for i in object_list:
        print (i.get_absolute_url)

    return render(request, 'cabinet/index.html', context)

def show_element(request,Management_name):
    object_list = cabinet.objects.filter(Management_name=Management_name)[0]
    name = Management_name
    path=settings.MEDIA_ROOT+ object_list.Mgment_path
    dir_list=[]
    for root, dirs, files in os.walk(path):
        for filename in files:
            dir_list.append(filename)

    context = {'object_list': object_list,'name':Management_name,'dir_list':dir_list}

    return render(request, 'cabinet/show_element.html', context)
