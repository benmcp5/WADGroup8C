# Generated by Django 4.0.3 on 2022-03-22 17:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ClubScoutGlasgow', '0018_auto_20220322_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewDate',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 17, 23, 18, 571195, tzinfo=utc)),
        ),
    ]
