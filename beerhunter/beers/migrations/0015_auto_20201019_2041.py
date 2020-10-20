# Generated by Django 3.0.9 on 2020-10-19 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0014_beercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='hunter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hunted', to=settings.AUTH_USER_MODEL),
        ),
    ]