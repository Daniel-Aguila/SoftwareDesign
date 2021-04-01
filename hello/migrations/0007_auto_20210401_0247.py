# Generated by Django 3.1.7 on 2021-04-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20210401_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware '), ('FL', 'Florida '), ('GA', 'Georgia '), ('HI', 'Hawaii '), ('ID', 'Idaho '), ('IL', 'Illinois '), ('IN', 'Indiana '), ('IA', 'Iowa '), ('KS', 'Kansas '), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine '), ('MD', 'Maryland '), ('MA', 'Massachusetts '), ('MI', 'Michigan '), ('MN', 'Minnesota '), ('MS', 'Mississippi '), ('MO', 'Missouri '), ('MT', 'Montana '), ('NE', 'Nebraska '), ('NV', 'Nevada '), ('NH', 'New Hampshire '), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio '), ('OK', 'Oklahoma '), ('OR', 'Oregon '), ('PA', 'Pennsylvania '), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee '), ('TX', 'Texas '), ('UT', 'Utah '), ('VT', 'Vermont '), ('VA', 'Virginia '), ('WA', 'Washington '), ('WV', 'West Virginia'), ('WI', 'Wisconsin '), ('WY', 'Wyoming')], max_length=2),
        ),
    ]
