# Generated by Django 3.0.9 on 2020-08-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hops', '0003_hop_aroma_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hop',
            options={'ordering': ('title',), 'verbose_name': 'Hop', 'verbose_name_plural': 'Hops'},
        ),
    ]
