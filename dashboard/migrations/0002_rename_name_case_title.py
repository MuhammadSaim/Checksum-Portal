# Generated by Django 4.2 on 2023-04-23 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='name',
            new_name='title',
        ),
    ]
