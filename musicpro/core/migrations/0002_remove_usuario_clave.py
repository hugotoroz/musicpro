# Generated by Django 4.1.3 on 2023-05-16 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='clave',
        ),
    ]