# Generated by Django 3.0.7 on 2020-06-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200605_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['order_number']},
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='order_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
