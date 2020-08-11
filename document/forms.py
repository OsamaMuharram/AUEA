from django.forms import ModelForm
from .models import *


class correspondence_form(ModelForm):
    class Meta:
        model = correspondence_document
        fields = '__all__'

class decision_form(ModelForm):
    class Meta:
        model = decision_document
        fields = '__all__'

class warrant_form(ModelForm):
    class Meta:
        model = warrant_document
        fields = '__all__'


class preparator_form(ModelForm):
    class Meta:
        model = report_document
        fields = '__all__'


class report_form(ModelForm):
    class Meta:
        model = report_document
        fields = '__all__'
