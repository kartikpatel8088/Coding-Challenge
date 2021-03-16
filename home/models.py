from django.db import models


# Create your models here.
class DataDB(models.Model):
    name = models.TextField(max_length=255)
    upload = models.ImageField(upload_to='images/')

