from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from ClubScoutGlasgow.models import UserProfile, Club, Review, login_required, staff_member_required
from ClubScoutGlasgow.forms import UserForm, UserProfileForm, ClubForm, ReviewForm
import random, string


# Create your views here.

def home(request):
    context_dict = {}
    clubs = Club.objects.order_by('-averageOverallRating')[:5]  # to be replaced
    context_dict['clubs'] = clubs
    image_list =[]

    for club in clubs:
        image_list.append(club.images)
    context_dict['images'] = image_list


    # MOVE INTO CLUB PAGE- CHANGE TO NAME = club.name
    '''
        # hive = Club.objects.get(name = 'Hive')
        # image_list = hive.images.all()
        # context_dict['images'] = image_list
        '''
    return render(request, 'ClubScoutGlasgow/home.html', context=context_dict)


def about(request):
    return render(request, 'ClubScoutGlasgow/about.html')


def user_login(request):  # copied from twd, maybe not compatible?
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('ClubScoutGlasgow:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            messages.ERROR: (request, "Invalid Login Details")
            return redirect(reverse('ClubScoutGlasgow:login'))
    else:
        return render(request, 'ClubScoutGlasgow/login.html')


def user_signup(request):  # copied from twd
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}

    return render(request, 'ClubScoutGlasgow/signup.html', context=context_dict)


def map(request):
    return render(request, 'ClubScoutGlasgow/map.html')


def clubs(request):  # yet to add sorting options?
    context_dict = {}
    try:
        club = Club.objects.order_by('name')
        context_dict['clubs'] = club
    except Club.DoesNotExist:
        context_dict['clubs'] = None
    return render(request, 'ClubScoutGlasgow/clubs.html',
                  context=context_dict)  # note clubs.html for whole list template, not club.html for individual


def show_club(request, club_name_slug):
    context_dict = {}
    try:
        club = Club.objects.get(slug=club_name_slug)
        
        image_list = club.images.all()
        context_dict['images'] = image_list
        review_list = Review.objects.filter(club = club)
        context_dict['reviews'] = review_list

        totalRating = 0
        counter = 0
        if review_list:

            for review in review_list:
                counter+=1
                totalRating += review.overallRating

            club.averageOverallRating = totalRating/(counter)
            club.save()
        context_dict['club'] = club
    except Club.DoesNotExist:
        context_dict['club'] = None
    except Review.DoesNotExist:
         context_dict['reviews'] = None


    return render(request, 'ClubScoutGlasgow/club.html', context=context_dict)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('ClubScoutGlasgow:home'))


def club_request(request):
    return render(request, 'ClubScoutGlasgow/club_request.html')


@login_required
def write_review(request, club_name_slug): 
    context_dict = {}
    try:
        club = Club.objects.get(slug=club_name_slug)
    except Club.DoesNotExist:
        club = None
    if club == None:
        return redirect('ClubScoutGlasgow/')

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if club:
                review = form.save(commit=False)
                review.club = club
                review.reviewer = UserProfile.objects.get(user=request.user)
                review.reviewLikes = 0
                review.reviewID = getReviewID(review.reviewer, review.club)
                review.save()

                review_list = Review.objects.filter(club = club)
                totalRating = 0
                counter = 0
                if review_list:

                    for review in review_list:
                        counter+=1
                        totalRating += review.overallRating

                    club.averageOverallRating = totalRating/(counter)
                    club.save()
                    
                
                return redirect(reverse('ClubScoutGlasgow:show_club', kwargs={'club_name_slug': club_name_slug}))

    else:
        print(form.errors)
    context_dict = {'form': form, 'club': club}
    return render(request, 'ClubScoutGlasgow/write_review.html', context=context_dict)


def getReviewID(reviewer, club):
    reviewID = ""
    reviewer = str(reviewer.user.username)
    club = club.name
    if len(reviewer) >= 6:
        reviewID += reviewer[:6]
    else:
        reviewID += reviewer + "%" * (6 - len(reviewer))

    for i in range(10):
        reviewID += random.choice(string.ascii_letters)

    if len(club) >= 6:
        reviewID += club[:6]
    else:
        reviewID += club + "%" * (6 - len(club))
    return reviewID


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

            # Now that the category is saved, we could confirm this. # For now, just redirect the user back to the index view.
            return redirect('/ClubScoutGlasgow/')
    else:
        # The supplied form contained errors -
        # just print them to the terminal.
        print(form.errors)
        # Will handle the bad form, new form, or no form supplied cases. # Render the form with error messages (if any).
    return render(request, 'ClubScoutGlasgow/add_club.html', {'form': form})
