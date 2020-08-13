import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from cabinet.models import managment
from .models import parent_document
from django.contrib.auth.decorators import login_required,permission_required
from .forms import *
from django.core.paginator import Paginator

@login_required
def index(request):

    document_list=parent_document.objects.all()
    paginator = Paginator(document_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'document_obj':page_obj,}

    return render(request, 'document/index.html', context)


#@permission_required('auth.delete_user')

@login_required
def document_type(request):

    context = {}
    return render(request, 'document/choose_document_type.html', context)


def display(request,id):
    obj_detail=parent_document.objects.get(id=id)
    context = {'obj_detail':obj_detail}
    return render(request, 'document/display_document.html', context)


@login_required
def add_warrant(request):
    if request.method == 'POST':
        myform = warrant_form(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
    else:
        myform = warrant_form()
    context = {'myform': myform}
    return render(request, 'document/add_warrant.html', context)


@login_required
def add_decision(request):
    if request.method == 'POST':
        myform = decision_form(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()

    else:
        myform = decision_form()
    context = {'myform': myform}
    return render(request, 'document/add_decision.html', context)

@login_required
def add_preparator(request):
    if request.method == 'POST':
        myform = preparator_form(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()

    else:
        myform = preparator_form()
    context = {'myform': myform}
    return render(request, 'document/add_preparator.html', context)

@login_required
def add_report(request):
    if request.method == 'POST':
        myform = report_form(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
    else:
        myform = report_form()
    context = {'myform': myform}
    return render(request, 'document/add_report.html', context)


@login_required
def add_correspondence(request):
    if request.method == 'POST':
        myform = correspondence_form(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            print('hoooooooooooooooooooooooo')

    else:
        myform = correspondence_form()
    context = {'myform': myform}
    return render(request, 'document/add_correspondence.html', context)