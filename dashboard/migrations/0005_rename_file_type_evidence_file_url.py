# Generated by Django 4.2 on 2023-04-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_evidence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='file_type',
            new_name='file_url',
        ),
    ]
