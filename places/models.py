from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=150)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Долгота', null=True)
    lat = models.FloatField('Широта', null=True)

    def __str__(self):
        return self.title
