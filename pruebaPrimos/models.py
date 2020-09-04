from django.db import models

class Primos(models.Model):

    numero = models.IntegerField(max_length=150, blank=False, default='')
    numeros_primos = models.CharField(max_length=150, blank=False, default='')




