# Generated by Django 4.0.5 on 2023-02-17 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_alter_retailer_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='name',
        ),
        migrations.AlterField(
            model_name='retailer',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
