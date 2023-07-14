from django.db import models

# Create your models here.
class Enviar(models.Model):
    arquivo = models.FileField(upload_to='/uploads/')