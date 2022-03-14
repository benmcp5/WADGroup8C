# Generated by Django 2.2.26 on 2022-03-10 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('entryPrice', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=100)),
                ('noOfRooms', models.IntegerField(default=0)),
                ('openingHours', models.DateTimeField()),
                ('averageOverallRating', models.FloatField(default=0)),
                ('website', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewID', models.CharField(max_length=30, unique=True)),
                ('drinksPrice', models.CharField(max_length=128)),
                ('typeOfCrowd', models.CharField(max_length=30)),
                ('popularNight', models.CharField(max_length=9)),
                ('avgQueueTime', models.IntegerField(default=0)),
                ('staffFriendliness', models.IntegerField(default=0)),
                ('qualityOfSafety', models.IntegerField(default=0)),
                ('overallRating', models.IntegerField(default=0)),
                ('additionalComments', models.CharField(max_length=500)),
                ('reviewLikes', models.IntegerField(default=0)),
                ('url', models.URLField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubScoutGlasgow.Club')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubScoutGlasgow.UserProfile')),
            ],
        ),
    ]
