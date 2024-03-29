# Generated by Django 3.0.9 on 2020-08-19 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
        ('beers', '0003_auto_20200819_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brewered_by', to='breweries.Brewery'),
        ),
    ]
