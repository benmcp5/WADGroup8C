from ClubScoutGlasgow.models import UserProfile, Club
from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_staff')

class UserProfileForm(forms.ModelForm):
     class Meta:
        model = UserProfile
        fields = ('age',)


class ClubForm(forms.ModelForm):
    name = forms.CharField(max_length=30,
                               help_text="Please enter the Club name.")
    entryPrice = forms.IntegerField(initial=0, help_text="Standard Entry")
    location = forms.CharField(max_length=100, help_text="Address")
    noOfRooms = forms.IntegerField(initial=1, help_text="How many rooms?")
    openingHours = forms.CharField(max_length=500, help_text = "Opening Hours")
    averageOverallRating = forms.FloatField(widget = forms.HiddenInput(), initial = 0)
    website = forms.URLField(help_text="Website")
    instagram = forms.URLField(help_text="Instagram")
    facebook = forms.URLField(help_text="Facebook")


    about = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),help_text="About this club" )

    def cleanF(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('facebook')
        # If url is not empty and doesn't start with 'http://', # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data[field] = url
        return cleaned_data

    def cleanI(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('instagram')
        # If url is not empty and doesn't start with 'http://', # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data[field] = url
        return cleaned_data

    def cleanW(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('website')
        # If url is not empty and doesn't start with 'http://', # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data[field] = url
        return cleaned_data

    # An inline class to provide
    class Meta:
    # Provide an association
        model = Club
        fields = ('name',)
