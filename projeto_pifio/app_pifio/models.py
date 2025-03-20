from django.db import models

# Create your models here.
class Pifios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)