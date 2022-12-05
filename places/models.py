from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=150)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Долгота', null=True)
    lat = models.FloatField('Широта', null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Относится к месту',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True)
    img = models.ImageField('Картинка', upload_to='', null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.place}'