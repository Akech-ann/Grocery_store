# Generated by Django 4.2.1 on 2023-06-17 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesperson', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='contacts',
            new_name='contact',
        ),
    ]