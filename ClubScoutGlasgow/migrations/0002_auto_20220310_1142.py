# Generated by Django 2.2.26 on 2022-03-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubScoutGlasgow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
