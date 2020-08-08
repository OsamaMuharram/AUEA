from django.db import models
from taggit.managers import TaggableManager
from cabinet.models import employee ,cabinet
# Create your models here.
def Management_path(instance, filename):
    return '{0}/{1}'.format(instance.select_cabinet, filename)

class document(models.Model):

    name=models.CharField(max_length=100)
    employee_name = models.ForeignKey('cabinet.employee',
                                      on_delete=models.CASCADE, )
    select_cabinet= models.ForeignKey('cabinet.cabinet',
                                      on_delete=models.CASCADE, )

    file_uploded = models.FileField(upload_to=Management_path)

    def __str__(self):
        return str(self.name)

class document_type(models.Model):
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    def __str__(self):
        return str(self.name)


class preparator_document(models.Model):
    title = models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    management_name = models.ForeignKey('cabinet.cabinet',
                                       on_delete=models.CASCADE, )
    boss_name=models.CharField(max_length=150)
    meeting_type=models.CharField(max_length=150)
    create_date = models.DateField()
    published = models.DateField(auto_now_add=True)
    tags=models
    def __str__(self):
        return str(self.title)