from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return str(self.name)
