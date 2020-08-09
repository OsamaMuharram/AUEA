from django.contrib import admin

from .models import document,document_type\
    ,preparator_document\
    ,report_document\
    ,Correspondence_document\
    ,decision_document\
    ,warrant_document\
# Register your models here.
admin.site.register(document)
admin.site.register(document_type)
admin.site.register(preparator_document)
admin.site.register(warrant_document)
admin.site.register(report_document)
admin.site.register(Correspondence_document)
admin.site.register(decision_document)
