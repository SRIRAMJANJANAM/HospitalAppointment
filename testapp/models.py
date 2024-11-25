from django.db import models

# Create your models here.
class Appointment(models.Model):
    pn=models.CharField(max_length=40)
    doc=models.CharField(max_length=40)
    date=models.DateField()
    time=models.TimeField()