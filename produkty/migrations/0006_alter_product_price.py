# Generated by Django 5.0.3 on 2024-05-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0005_alter_product_name_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
