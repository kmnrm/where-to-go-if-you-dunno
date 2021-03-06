# Generated by Django 3.0.7 on 2020-06-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
