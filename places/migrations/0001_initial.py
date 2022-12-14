# Generated by Django 3.2.16 on 2022-12-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название места')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_long', models.TextField(verbose_name='Длинное описание')),
                ('lng', models.FloatField(null=True, verbose_name='Долгота')),
                ('lat', models.FloatField(null=True, verbose_name='Широта')),
            ],
        ),
    ]
