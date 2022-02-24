from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=128)
    mark = models.TextField(blank=True)
    manufacturer = models.TextField(verbose_name='История', blank=True)

    def __str__(self):
        return f'{self.name}, <{self.mark}>'

