from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=150, unique=True)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Относится к месту',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True)
    img = models.ImageField('Картинка')
    imagetitle = models.CharField(
        'Название изображения',
        max_length=70,
        null=True,
        unique=True,
        )
    my_order = models.PositiveIntegerField('Порядок', default=1)

    class Meta:
        ordering = ['my_order']

    @property
    def get_absolute_image_url(self):
        return self.img.url

    def __str__(self):
        return f'{self.id} {self.place}'