# Generated by Django 3.0.9 on 2020-08-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title of brewery'),
        ),
    ]