# Generated by Django 4.0.3 on 2022-03-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubScoutGlasgow', '0010_auto_20220317_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='openingHours',
            field=models.TextField(default='Monday:\nTuesday:\nWednesday:\nThursday:\nFriday:\nSaturday:\nSunday:', max_length=500),
        ),
    ]
