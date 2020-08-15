import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


from cabinet.models import managment
# Create your models here.
def Management_path(instance, filename):
    return '{0}/{1}'.format(instance.select_cabinet, filename)



class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class parent_document(models.Model):
    title = models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    event_date = models.DateField()
    published_at= models.DateField(auto_now_add=True)
    select_managment = models.ForeignKey('cabinet.managment',
                                       on_delete=models.CASCADE, )

    select_tag = models.ManyToManyField('Tags')
    file_uploded = models.FileField(upload_to=Management_path)
    slug=models.SlugField(blank=True,null=True)


    def save(self, *args,**kwargs):
        d=self.event_date
        self.slug=slugify(str(d.year)+str(d.month)+str(self.id))
        super(parent_document,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)



    """////////////////////////////////////////"""
    """
    create preparator table 

    """
class preparator_document(parent_document):
    boss_name=models.CharField(max_length=150)
    meeting_type=models.CharField(max_length=150)

    """
    create decision_document table 
    """
class decision_document(parent_document):
    Issuer=models.CharField(max_length=150)
    decision_type=models.CharField(max_length=150)

    """
    create Correspondence_document table 
    """
class correspondence_document(parent_document):
    Issuer=models.CharField(max_length=150)
    Destination=models.CharField(max_length=150)

    """
    create report_document table
    """

class report_document(parent_document):
    #جهة الاصدار
    Issuer=models.CharField(max_length=150)
    Destination=models.CharField(max_length=150)

    """
    create warrant_document table 
    """
class warrant_document(parent_document):
    #جهة الاصدار
    Issuer_creator=models.CharField(max_length=150)
    Destination=models.CharField(max_length=150)
""""///////////////////////////////////////////////"""