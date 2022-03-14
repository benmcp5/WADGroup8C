from django.shortcuts import render, redirect
from django.http import HttpResponse
from ClubScoutGlasgow.models import UserProfile, Club, Review, login_required, staff_member_required
from ClubScoutGlasgow.forms import UserForm, UserProfileForm, ClubForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

def home(request):
        context_dict = {}
        clubs = Club.objects.order_by('-name')[:5]
        context_dict['clubs'] = clubs
        return render(request, 'ClubScoutGlasgow/home.html', context=context_dict)

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
                # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid(): # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and #put it in the UserProfile model.

            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to indicate that the template # registration was successful.
            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
            # Render the template depending on the context.
    return render(request, 'ClubScoutGlasgow/register.html',
                      context = {'user_form': user_form,
                                 'profile_form': profile_form,
                                 'registered': registered})


def show_club(request, club_name_slug):
    context_dict={}
    try:
        club  = club.objects.get(slug = club_name_slug)
        context_dict['club'] = club

    except Club.DoesNotExist:
        context_dict['club'] = None

    return render(request, 'ClubScoutGlasgow/club.html', context = context_dict)

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed
            # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>'] # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in. # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('ClubScoutGlasgow:home'))
            else:
            # An inactive account was used - no logging in!
                return HttpResponse("Your ClubScoutGlasgow account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'ClubScoutGlasgow/login.html')
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'ClubScoutGlasgow/login.html')


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('ClubScoutGlasgow:home'))

@staff_member_required
def add_club(request):

    form = ClubForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = ClubForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            print("-BCBCVJBCVJC")
            # Now that the category is saved, we could confirm this. # For now, just redirect the user back to the index view.
            return redirect('/ClubScoutGlasgow/')
    else:
        # The supplied form contained errors -
         # just print them to the terminal.
        print(form.errors)
        # Will handle the bad form, new form, or no form supplied cases. # Render the form with error messages (if any).
    return render(request, 'ClubScoutGlasgow/add_club.html', {'form': form})
