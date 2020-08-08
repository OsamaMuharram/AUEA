from django.contrib import admin

from .models import document,document_type,preparator_document
# Register your models here.
admin.site.register(document)
admin.site.register(document_type)
admin.site.register(preparator_document)