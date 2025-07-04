# Generated by Django 5.0.6 on 2025-02-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('kg', 'kilogram'), ('g', 'gram'), ('L', 'liter'), ('mL', 'milliliter'), ('', 'no_unit')], default='', max_length=2),
        ),
    ]
