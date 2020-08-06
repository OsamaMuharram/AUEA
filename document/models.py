from django.db import models

from cabinet.models import employee ,cabinet
# Create your models here.
def Management_path(instance, filename):
    return '{0}/{1}'.format(instance.select_cabinet, filename)

class document(models.Model):
    name=models.CharField(max_length=20)
    employee_name = models.ForeignKey('cabinet.employee',
                                      on_delete=models.CASCADE, )
    select_cabinet= models.ForeignKey('cabinet.cabinet',
                                      on_delete=models.CASCADE, )


    file_uploded = models.FileField(upload_to=Management_path)

    def __str__(self):
        return str(self.name)