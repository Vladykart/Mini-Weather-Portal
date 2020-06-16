# Generated by Django 3.0.7 on 2020-06-14 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20200614_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='icon',
            field=models.CharField(default='', max_length=25, null=True),
        ),
    ]
