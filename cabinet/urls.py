from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1,name='index1'),
    path('<str:Management_name>/', views.show_element, name='show_element'),


]
