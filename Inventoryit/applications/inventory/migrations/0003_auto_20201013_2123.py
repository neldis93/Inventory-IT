# Generated by Django 3.0.8 on 2020-10-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20201013_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='model',
            field=models.CharField(choices=[('0', 'Portatil'), ('1', 'Sobremesa'), ('2', 'Surface')], max_length=1, verbose_name='Model'),
        ),
    ]
