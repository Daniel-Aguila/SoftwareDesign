# Generated by Django 3.1.7 on 2021-04-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20210331_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='fullAddress',
            field=models.CharField(max_length=100),
        ),
    ]