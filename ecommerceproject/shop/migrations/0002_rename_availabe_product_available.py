# Generated by Django 4.1.1 on 2022-10-17 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availabe',
            new_name='available',
        ),
    ]
