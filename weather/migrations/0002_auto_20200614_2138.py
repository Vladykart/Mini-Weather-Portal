# Generated by Django 3.0.7 on 2020-06-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AddField(
            model_name='city',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=4),
        ),
    ]