# Generated by Django 3.0.8 on 2020-10-13 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['id'], 'verbose_name': 'Inventory'},
        ),
    ]
