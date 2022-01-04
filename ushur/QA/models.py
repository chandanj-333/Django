from django.db import models

# Create your models here.
class Training(models.Model):
    name=models.CharField(max_length=10, unique=True)
    noteslink=models.TextField(unique=True)
    videolink=models.TextField(unique=True)