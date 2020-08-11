from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('test/', views.test, name='test'),
    path('add/', views.document_type, name='document_type'),
    path('add/warrant/', views.add_warrant, name='add_warrant_document'),
    path('add/decision/', views.add_decision, name='add_decision_document'),
    path('add/correspondence/', views.add_correspondence, name='add_correspondence_document'),
    path('add/report/', views.add_report, name='add_report_document'),
    path('add/preparator/', views.add_preparator, name='add_preparator_document'),



]
