# Generated by Django 3.0.9 on 2020-08-21 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0005_auto_20200820_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='hunter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
