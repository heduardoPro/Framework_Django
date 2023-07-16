from django.db import models

# Create your models here.
class Arquivo(models.Model):
    arquivo = models.ImageField()