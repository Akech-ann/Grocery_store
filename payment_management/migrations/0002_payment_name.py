# Generated by Django 4.2.1 on 2023-06-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
