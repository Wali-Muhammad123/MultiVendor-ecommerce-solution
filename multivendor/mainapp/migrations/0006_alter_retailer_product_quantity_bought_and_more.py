# Generated by Django 4.0.5 on 2023-02-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_retailer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer_product',
            name='quantity_bought',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='retailer_product',
            name='quantity_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
