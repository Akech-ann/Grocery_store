# Generated by Django 4.2.3 on 2023-08-18 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartmanager', '0003_cart_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='name',
        ),
    ]
