# Generated by Django 3.0.7 on 2020-06-07 12:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20200606_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(verbose_name='Координаты широты'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(verbose_name='Координаты долготы'),
        ),
    ]