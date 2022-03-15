from django.urls import path
from ClubScoutGlasgow import views

app_name = 'ClubScoutGlasgow'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('map/', views.map, name='map'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/request-a-club/', views.club_request, name='club_request'),
    path('club/<slug:club_name_slug>/', views.show_club, name='show_club'),
    path('club/<slug:club_name_slug>/write_review', views.write_review, name='write_review'),
    path('add_club/', views.add_club, name='add_club'),
]
