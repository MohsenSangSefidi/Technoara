# Generated by Django 5.0.7 on 2024-08-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0003_productmodel_product_sale_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیر فعال'),
        ),
    ]
