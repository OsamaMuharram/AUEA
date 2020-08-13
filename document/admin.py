from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(parent_document)
admin.site.register(preparator_document)
admin.site.register(warrant_document)
admin.site.register(report_document)
admin.site.register(correspondence_document)
admin.site.register(decision_document)
admin.site.register(Tags)