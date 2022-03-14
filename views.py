from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ClubScoutGlasgow.models import UserProfile, Club, Review, login_required, staff_member_required
from ClubScoutGlasgow.forms import UserForm, UserProfileForm, ClubForm
# Create your views here.

def home(request):
        context_dict = {}
        clubs = Club.objects.order_by('-name')[:5] #to be replaced
        context_dict['clubs'] = clubs
        return render(request, 'ClubScoutGlasgow/home.html', context=context_dict)
    
def about(request):
    return render(request, 'ClubScoutGlasgow/about.html')
    
def user_login(request): #copied from twd, maybe not compatible?
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('ClubScoutGlasgow:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'ClubScoutGlasgow/login.html')
        
def user_signup(request): #copied from twd
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
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'ClubScoutGlasgow/register.html', context = {'user_form': user_form,'profile_form': profile_form, 'registered': registered})

def map(request):
    return render(request, 'ClubScoutGlasgow/map.html')

def clubs(request, club_name_slug): #yet to add sorting options?
    context_dict = {}
    try:
        club = Clubs.objects.order_by('name')
        context_dict['club'] = club
    except Clubs.DoesNotExist:
        context_dict['club'] = None
    return render(request, 'ClubScoutGlasgow/clubs.html', context=context_dict) #note clubs.html for whole list template, not club.html for individual

def show_club(request, club_name_slug):
    context_dict={}
    try:
        club  = club.objects.get(slug = club_name_slug)
        context_dict['club'] = club

    except Club.DoesNotExist:
        context_dict['club'] = None

    return render(request, 'ClubScoutGlasgow/club.html', context = context_dict)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('ClubScoutGlasgow:home'))

def club_request(request):
    return render(request, 'ClubScoutGlasgow/club_request.html')

def write_review(request, club_name_slug): #no ReviewForm yet
    context_dict = {}
    try:
        club = Club.objects.get(slug = club_name_slug)
    except Club.DoesNotExist:
        club = None
    if club == None:
        return redirect('ClubScoutGlasgow/')
    
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            print("-BCBCVJBCVJC")
            return redirect('/ClubScoutGlasgow/')
    else:
        print(form.errors)
    return render(request, 'ClubScoutGlasgow/write_review.html', context = context_dict)

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


