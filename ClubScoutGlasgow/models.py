from django.db import models
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core import validators
import django.utils.timezone
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.PositiveIntegerField(default=18)

    def __str__(self):
        return self.user.username


class Club(models.Model):
    name = models.CharField(max_length=30, unique=True)
    entryPrice = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    noOfRooms = models.PositiveIntegerField(default=1)
    openingString = """Monday:
Tuesday:
Wednesday:
Thursday:
Friday:
Saturday:
Sunday:"""
    openingHours = models.TextField(max_length=500, default=openingString)
    averageOverallRating = models.FloatField(default=0)
    instagram = models.URLField(default="https://www.instagram.com")
    facebook = models.URLField(default="https://www.facebook.com")
    website = models.URLField(default="https://www.")
    mapSrc = models.URLField(default="https://maps.google.com/maps?q=firewater&t=&z=13&ie=UTF8&iwloc=&output=embed")
    about = models.TextField(max_length=500, default="")
    #menu = models.FileField(upload_to='static/Menu/', default="")

    slug = models.SlugField(unique=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Club, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClubImage(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/ClubImages/')
    imageName = image.upload_to.split('/')
    imageName = imageName[2]
    url = models.CharField(max_length=500, default='images/ClubImages/' + str(imageName))


class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    reviewID = models.CharField(max_length=30, unique=True)
    reviewDate = models.DateField(default=django.utils.timezone.now())

    drinksPrice = models.IntegerField(default=1)
    typeOfCrowd = models.CharField(max_length=30)
    popularNight = models.CharField(max_length=9)
    avgQueueTime = models.IntegerField(default=0)
    staffFriendliness = models.IntegerField(default=1)
    qualityOfSafety = models.IntegerField(default=1)
    overallRating = models.IntegerField(default=1)
    additionalComments = models.CharField(max_length=1000, default = "")
    reviewLikes = models.IntegerField(default=0)

    def __str__(self):
        return self.reviewID
