# Generated by Django 3.0.7 on 2020-06-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_auto_20200614_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.CharField(default='', max_length=25, null=True),
        ),
    ]
