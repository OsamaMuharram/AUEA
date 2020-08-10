import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from cabinet.models import cabinet
from .models import document,document_type,parent_document


def index(request):
    cabinet_list = cabinet.objects.all()
    document_list=parent_document.objects.all()
    path = settings.MEDIA_ROOT

    context={'document_list':document_list,'path':path,'cabinet_list':cabinet_list}

    return render(request, 'document/index.html', context)

def test(request):
    cabinet_list = cabinet.objects.all()
    document_list=parent_document.objects.all()
    path = settings.MEDIA_ROOT

    context={'document_list':document_list,'path':path,'cabinet_list':cabinet_list}

    return render(request, 'document/test.html', context)
