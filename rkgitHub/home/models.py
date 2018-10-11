from django.db import models

# Create your models here.

class Carousal(models.Model):
    image=models.ImageField(upload_to="{}".format('home/carousal/'))
    descriptionHead=models.TextField(max_length=50,default="")
    descriptionBody=models.TextField(max_length=100,default="")
    registerText = models.CharField(max_length=50, default="")
    link=models.CharField(max_length=100,default="")