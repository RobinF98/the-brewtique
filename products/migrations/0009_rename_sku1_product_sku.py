# Generated by Django 5.0.6 on 2025-02-22 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_sku_product_sku1_alter_product_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sku1',
            new_name='sku',
        ),
    ]
