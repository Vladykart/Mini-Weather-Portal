# Generated by Django 3.0.7 on 2020-06-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_auto_20200614_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='description',
        ),
        migrations.RemoveField(
            model_name='city',
            name='icon',
        ),
    ]