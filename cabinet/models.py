from django.db import models


# Create your models here.


class cabinet(models.Model):

    Management_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    branuch_from = models.ForeignKey('self',  on_delete=models.SET_NULL,
    blank=True,
    null=True,)

    employee = models.ForeignKey(
        'employee',
        on_delete=models.CASCADE,
    )
    #الحقل الخاص بالمسارات متفرع من branuch from
    Mgment_path = models.CharField(max_length=200,null=True,blank=True )

    #دالة الحصول على اسم الادارة من البرانش فروم واضافتها فى المسار

    def save(self, *args, **kwargs):
        if str(self.branuch_from) == 'None':
            self.Mgment_path = '' + str(self.Management_name)
            super().save(*args, **kwargs)
        else:
            self.Mgment_path = str(self.branuch_from) + '/' + str(self.Management_name)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.Mgment_path)


#كلاس الموظفين
class employee(models.Model):

    employee_name = models.CharField(max_length=50)
    def __str__(self):

        return str(self.employee_name)


