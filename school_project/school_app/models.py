from django.db import models


# Create your models here.

class clsdetails(models.Model):
    class_name = models.CharField(max_length=250)
    list_of_student = models.CharField(max_length=20)
    section = models.CharField(max_length=20)


class students(models.Model):
    student_name = models.CharField(max_length=25)
    student_age = models.IntegerField(default=0)
    father_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
