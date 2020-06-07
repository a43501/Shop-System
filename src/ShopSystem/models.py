from django.db import models

# Create your models here.
#数据库
class goods(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name= models.CharField(max_length=30)
    count= models.IntegerField()
    price= models.FloatField()