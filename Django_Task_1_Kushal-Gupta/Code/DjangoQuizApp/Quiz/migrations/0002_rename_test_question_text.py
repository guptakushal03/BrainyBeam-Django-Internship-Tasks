# Generated by Django 4.2.5 on 2024-11-13 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test',
            new_name='text',
        ),
    ]
