# Generated by Django 4.2.3 on 2023-07-10 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesperson', '0002_rename_contacts_vendor_contact'),
        ('inventory', '0003_delete_customer_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salesperson.vendor'),
            preserve_default=False,
        ),
    ]
