from django.db import models

# Create your models here.
class Patient00(models.Model):
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    alter = models.IntegerField(null=True)
    motif = models.TextField(null=True)
    ladate=models.DateTimeField(auto_now=True)