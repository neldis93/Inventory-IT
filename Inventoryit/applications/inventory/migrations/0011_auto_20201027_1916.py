# Generated by Django 3.0.8 on 2020-10-27 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20201025_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changecontrol',
            options={'ordering': ['tracing_number'], 'verbose_name': 'Change control'},
        ),
        migrations.RenameField(
            model_name='changecontrol',
            old_name='tracing',
            new_name='tracing_number',
        ),
    ]
