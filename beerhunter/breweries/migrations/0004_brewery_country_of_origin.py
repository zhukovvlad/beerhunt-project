# Generated by Django 3.0.9 on 2020-08-21 09:09

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0003_auto_20200820_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of Origin'),
        ),
    ]
