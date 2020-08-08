import uuid
from django.db import models
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




class parent_document(models.Model):
    title = models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    management_name = models.ForeignKey('cabinet.cabinet',
                                       on_delete=models.CASCADE, )
    event_date = models.DateField()
    published = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('tags.Tags')
    class Meta:
        abstract = True
    def __str__(self):
        return str(self.title)



    """
     /
    /
    /
    create preparator table 
    /
    /
    /
    """
class preparator_document(parent_document):
    boss_name=models.CharField(max_length=150)
    meeting_type=models.CharField(max_length=150)
    def __str__(self):
        return str(self.title)


    """
     /
    /
    /
    create decision_document table 
    /
    /
    /
    """
class decision_document(parent_document):
    boss_name=models.CharField(max_length=150)
    decision_type=models.CharField(max_length=150)
    def __str__(self):
        return str(self.title)


    """
     /
    /
    /
    create Correspondence_document table 
    /
    /
    /
    """
class Correspondence_document(parent_document):
    Issuer=models.CharField(max_length=150)
    Destination=models.CharField(max_length=150)
    def __str__(self):
        return str(self.title)



    """
    /
    /
    /
    /
    
    create report_document table
    /
    /
    /
    /
    """

class report_document(parent_document):
    #جهة الاصدار
    Issuer=models.CharField(max_length=150)
    Destination=models.CharField(max_length=150)
    def __str__(self):
        return str(self.title)

    """
     /
    /
    /
    create warrant_document table 
    /
    /
    /
    """

class warrant_document(parent_document):
    warrant_creator = models.CharField(max_length=150)
    Destination = models.CharField(max_length=150)

    def __str__(self):
        return str(self.title)

