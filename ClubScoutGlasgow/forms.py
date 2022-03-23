from ClubScoutGlasgow.models import *
from django import forms
from django.contrib.auth.models import User
from django.core import validators

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(),
    validators = [validators.MinLengthValidator(6)] )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField(validators =[validators.MinValueValidator(18)])
    class Meta:
        model = UserProfile
        fields = ('age',)


class ClubForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=30,
        help_text="Please enter the Club name.")
    entryPrice = forms.IntegerField(required=True, initial=0, help_text="Standard Entry")
    location = forms.CharField(required=True, max_length=100, help_text="Address")
    noOfRooms = forms.IntegerField(required=True, initial=1, help_text="How many rooms?",
        validators = [validators.MinValueValidator(1)])
    openingString = "Monday:\nTuesday:\nWednesday:\nThursday:\nFriday:\nSaturday:\nSunday:"
    openingHours = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 7, 'cols': 40}),
            help_text="Opening Hours", initial = openingString )
    averageOverallRating = forms.FloatField(required=True, widget = forms.HiddenInput(), initial = 0)
    website = forms.URLField(required=True, help_text="Website")
    instagram = forms.URLField(required=True, help_text="Instagram")
    facebook = forms.URLField(required=True, help_text="Facebook")
    about = forms.CharField(required=True,max_length=1000, widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}), help_text="About this club" )

    # An inline class to provide
    class Meta:
    # Provide an association
        model = Club
        fields = ('name',)


class ReviewForm(forms.ModelForm):

    drinksPrice = forms.IntegerField(required=True, validators = [validators.MinValueValidator(1), validators.MaxValueValidator(5)],
        initial =1, help_text = 'Out of 5, how expensive were the drinks?\nWith 5 being the most expensive and 1 being the cheapest')
    typeOfCrowd = forms.CharField(required=True, max_length=30,
        help_text = 'One word to describe the type of people at the club:')
    popularNight = forms.CharField(required=True, max_length = 9,
        help_text = 'What night is most popular:')
    avgQueueTime = forms.IntegerField(required=True, initial = 0, validators = [validators.MinValueValidator(0)],
        help_text = 'How many minutes did you have to queue for?')
    staffFriendliness = forms.IntegerField(required=True, initial = 1, validators = [validators.MinValueValidator(1), validators.MaxValueValidator(5)],
        help_text = 'Out of 5 how friendly were the staff?')
    qualityOfSafety = forms.IntegerField(required=True, initial = 1, validators = [validators.MinValueValidator(1), validators.MaxValueValidator(5)],
        help_text = 'Out of 5, how safe did you feel?\nWith 5 being extremely safe:')
    overallRating = forms.IntegerField(required=True, initial = 1, validators = [validators.MinValueValidator(1), validators.MaxValueValidator(5)],
        help_text = 'Rate your experience out of 5:')
    additionalComments = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}),
        help_text="Describe your experience:" )

    class Meta:
    # Provide an association
        model = Review
        exclude = ('club','reviewer', 'reviewDate', 'reviewID', 'reviewLikes')
