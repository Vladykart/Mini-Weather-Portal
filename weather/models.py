from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=25)
    temperature = models.DecimalField(decimal_places=2, max_digits=4, default=None, null=True)
    description = models.CharField(max_length=60, default='', null=True)
    icon = models.CharField(max_length=25, default='', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'cities'
