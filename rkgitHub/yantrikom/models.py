from django.db import models

# Create your models here.

class News(models.Model):
    circular=models.TextField(max_length=300)
    pdf=models.FileField(upload_to="{}".format('yantrikom/circular/'),blank=True)
class Carousal(models.Model):
    image=models.ImageField(upload_to="{}".format('yantrikom/carousal/'))
    descriptionHead=models.TextField(max_length=50,default="")
    descriptionBody=models.TextField(max_length=100,default="")
    registerText = models.CharField(max_length=50, default="")
    link=models.CharField(max_length=100,default="")

class Fame(models.Model):
    branch_choice = (
    ('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('EEE', 'EEE'), ('MBA', 'MBA'), ('MCA', 'MCA'),
    ('B.Pharma', 'B.Pharma'))
    name = models.CharField(max_length=50, default="")
    branch = models.CharField(max_length=10, default="CSE", choices=branch_choice)
    year_choice=(('First Year','I'),('Second Year','II'),('Third Year','III'),('Fourth Year','IV'))
    year=models.CharField(max_length=15,default='',choices=year_choice)
    image=models.ImageField(upload_to="{}".format('yantrikom/fame/'))
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name+' '+self.branch+"("+self.year+")"
class Core(models.Model):
    branch_choice=(('CSE','CSE'),('IT','IT'),('ECE','ECE'),('ME','ME'),('EEE','EEE'),('MBA','MBA'),('MCA','MCA'),('B.Pharma','B.Pharma'))
    year_choice=(('First Year','I'),('Second Year','II'),('Third Year','III'),('Fourth Year','IV'))
    name=models.CharField(max_length=50)
    branch = models.CharField(max_length=10, default="CSE", choices=branch_choice)
    year=models.CharField(max_length=15,default='',choices=year_choice)
    image=models.ImageField(upload_to='yantrikom/core/')

    def __str__(self):
        return self.name + ' ' + self.branch + "(" + self.year + ")"