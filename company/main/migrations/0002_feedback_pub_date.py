# Generated by Django 5.0.4 on 2024-05-09 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(1900, 1, 1)),
            preserve_default=False,
        ),
    ]
