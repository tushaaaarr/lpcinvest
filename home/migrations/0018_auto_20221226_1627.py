# Generated by Django 3.1.7 on 2022-12-26 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20221226_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='area',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='constructionupdates',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 16, 27, 44, 693243)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 26, 16, 27, 44, 676708)),
        ),
    ]