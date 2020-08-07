from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('display/',views.display_document,name='display'),
    path('display/<str:file>', views.display_selected_document, name='display'),
]
