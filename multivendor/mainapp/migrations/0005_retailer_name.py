# Generated by Django 4.0.5 on 2023-02-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_retailer_name_alter_retailer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
