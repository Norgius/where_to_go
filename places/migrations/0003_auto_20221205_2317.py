# Generated by Django 3.2.16 on 2022-12-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Уникальный идентификатор'),
        ),
        migrations.AddField(
            model_name='place',
            name='short_title',
            field=models.CharField(max_length=70, null=True, verbose_name='Короткое название'),
        ),
    ]
