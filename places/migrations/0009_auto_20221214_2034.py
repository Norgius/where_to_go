# Generated by Django 3.2.16 on 2022-12-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20221214_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='my_order',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='image',
            name='imagetitle',
        ),
    ]