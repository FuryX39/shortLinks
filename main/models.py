from django.db import models


class Link(models.Model):

    full_link = models.CharField(max_length=511, verbose_name='Full link')
    short_id = models.CharField(max_length=15, verbose_name='Short ID')
    count = models.PositiveIntegerField(default=0, verbose_name='Redirect counter')

    def __str__(self):
        return f'{self.full_link} - {self.short_id}'
