from django.db import models

# Create your models here.
class Record(models.Model):
	nombre = models.CharField(max_length=30)
	fecha = models.DateTimeField()
	placas = models.CharField(max_length=30)