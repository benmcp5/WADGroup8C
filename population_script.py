import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WADGroup8C.settings')

django.setup()

from django.contrib.auth.models import User
from ClubScoutGlasgow.models import Club, Review, UserProfile


def populate():
    """
    templates

     club:
    "" : {
            "location": "",
            "openingHours": "",
            "website": "",
            "instagram": "",
            "facebook": "",
            "about": "",
        }

    """

    # Key is username
    users = {
        "user1": {
            "email": "user1@gmail.com",
            "age": 23,
        },
        "user2": {
            "email": "user2@gmail.com",
            "age": 80,
        },
        "user3": {
            "email": "user3@gmail.com",
            "age": 18,
        },
        "user4": {
            "email": "user4@gmail.com",
            "age": 21,
        },
        "user5": {
            "email": "user5@gmail.com",
            "age": 19,
        },
        "user6": {
            "email": "user6@gmail.com",
            "age": 19,
        },
        "user7": {
            "email": "user7@gmail.com",
            "age": 37,
        },
    }

    # Key is name of club
    clubs = {
        "Sub Club": {
            "EntryPrice": 8,
            "location": "22 Jamaica Street",
            "openingHours": "23:00-3:00",
            "website": "https://subclub.co.uk/",
            "instagram": "https://www.instagram.com/subclub87/",
            "facebook": "https://www.facebook.com/subclub",
            "mapSrc": "https://maps.google.com/maps?q=Sub%20Club&t=&z=13&ie=UTF8&iwloc=&output=embed",
            "about": "The Sub Club is a club and music venue located at 22 Jamaica Street in Glasgow, Scotland."
                     " It opened 1 April 1987 and is the longest running underground dance club in the world."
                     " The 3,500-square-foot (330 m2) basement space can legally hold up to 410 people."
                     " In 2008 it was voted the 10th best club in the world by Resident Advisor (and 5th "
                     "for atmosphere) and the 30th best club in the world by DJ Mag. In 2009 the club was placed"
                     " 14th best in the world by DJ Mag.",
        },
        "The Garage": {
            "EntryPrice": 4,
            "location": "490 Sauchiehall St",
            "openingHours": "23:00-3:00",
            "website": "https://garageglasgow.co.uk/",
            "instagram": "https://www.instagram.com/thegarageglasgow/",
            "facebook": "https://www.facebook.com/garageglasgow/",
            "mapSrc": "https://maps.google.com/maps?q=The%20Garage%20490%20Sauchiehall%20St&t=&z=13&ie=UTF8&iwloc=&output=embed",
            "about": "The Garage (formerly known as The Mayfair) is a music venue and nightclub located at 490 "
                     "Sauchiehall Street in Glasgow, Scotland. It is Scotland's largest nightclub. The main "
                     "hall was the first Locarno ballroom in the UK, although it has since been remodelled by "
                     "the addition of an extension to the mezzanine level. The Garage is made up of various rooms "
                     "which play different genres of music which are all accessed under one roof. The Main hall, "
                     "the biggest room, plays chart and remixes, G2 plays RnB hits, Desperados bar plays cheesy "
                     "and nostalgia while the final room The Attic plays indie and rock. There is also a shot and "
                     "cocktail bar at the back of Desperados bar. ",
        },
        "Nice \'N\' Sleazy": {
            "EntryPrice": 7,
            "location": "421 Sauchiehall St, Glasgow G2 3LG",
            "openingHours": "18:00-3:00",
            "website": "https://www.nicensleazy.com/",
            "instagram": "https://www.instagram.com/nicensleazy/",
            "facebook": "https://www.facebook.com/nicensleazyglasgow/",
            "mapSrc": "https://maps.google.com/maps?q=nice%20n%20sleazy&t=&z=13&ie=UTF8&iwloc=&output=embed",
            "about": "Buzzing bar with poster plastered walls and small capacity creating atmospheric musical "
                     "intimacy.",
        },
        "SWG3": {
            "EntryPrice": 16.50,
            "location": "100 Eastvale Pl, Stobcross Rd, Glasgow G3 8QG",
            "openingHours": "10:00-18:00",
            "website": "https://swg3.tv/",
            "instagram": "https://www.instagram.com/swg3glasgow/",
            "facebook": "https://www.facebook.com/SWG3glasgow/",
            "mapSrc": "https://maps.google.com/maps?q=swg3&t=&z=13&ie=UTF8&iwloc=&output=embed",
            "about": "SWG3 (Studio Warehouse Glasgow) is a multi-disciplinary arts space in the westend of Glasgow. "
                     "We run an annual programme of exhibitions, band nights and events as well as being home to a "
                     "community of over 120 artists and musicians.",
        },
        "Firewater": {
            "EntryPrice": 6,
            "location": "341 Sauchiehall St, Glasgow G2 3HW",
            "openingHours": "19:00-03:00",
            "website": "https://www.facebook.com/firewaterglasgowofficial",
            "instagram": "https://www.instagram.com/firewater_glasgow/?hl=en",
            "facebook": "https://www.facebook.com/firewaterglasgowofficial",
            "mapSrc": "https://maps.google.com/maps?q=firewater&t=&z=13&ie=UTF8&iwloc=&output=embed",
            "about": "Firewater offers Funk, Punk Rock’n’Roll and Disco in two rooms, under one roof"
                     " since 2001. Famed for legendary rock'n'roll-indie club nights and hosting huge"
                     " after-show parties.",
        }
    }

    # Key is review ID
    reviews = [
        {
            "reviewer": 1,
            "club": 4,
            "typeOfCrowd": "trendy",
            "popularNight": "Saturday",
            "avgQueueTime": 45,
            "staffFriendliness": 1,
            "qualityOfSafety": 4,
            "overallRating": 3,
            "additionalComments": "do not want",
        },
        {
            "reviewer": 7,
            "club": 4,
            "typeOfCrowd": "youthful",
            "popularNight": "Saturday",
            "avgQueueTime": 30,
            "staffFriendliness": 2,
            "qualityOfSafety": 2,
            "overallRating": 2,
            "additionalComments": "",
        },
        {
            "reviewer": 6,
            "club": 2,
            "typeOfCrowd": "the worst",
            "popularNight": "Friday",
            "avgQueueTime": 60,
            "staffFriendliness": 1,
            "qualityOfSafety": 1,
            "overallRating": 1,
            "additionalComments": "",
        },
        {
            "reviewer": 6,
            "club": 1,
            "typeOfCrowd": "everyone",
            "popularNight": "Saturday",
            "avgQueueTime": 15,
            "staffFriendliness": 4,
            "qualityOfSafety": 3,
            "overallRating": 4,
            "additionalComments": "class",
        },
    ]

    club_array = []
    for club in clubs:
        data = clubs[club]
        c = add_club(club, data)
        club_array.append(c)

    user_array = []
    for user in users:
        u = add_user(user, users[user])
        user_array.append(u)

    for review in reviews:
        club_id = club_array[review["club"] - 1]
        user_id = user_array[review["reviewer"] - 1]
        add_review(review, club_id, user_id)


def add_review(data, club_id, user_id):
    r = Review.objects.get_or_create(club=club_id, reviewer=user_id)[0]
    r.typeOfCrowd = data["typeOfCrowd"]
    r.popularNight = data["popularNight"]
    r.avgQueueTime = data["avgQueueTime"]
    r.staffFriendliness = data["staffFriendliness"]
    r.qualityOfSafety = data["qualityOfSafety"]
    r.overallRating = data["overallRating"]
    r.additionalComments = data["additionalComments"]
    r.save()
    return r


def add_club(name, data):
    c = Club.objects.get_or_create(name=name)[0]
    c.location = data["location"]
    c.openingHours = data["openingHours"]
    c.website = data["website"]
    c.instagram = data["instagram"]
    c.mapSrc = data["mapSrc"]
    c.facebook = data["facebook"]
    c.about = data["about"]
    c.save()
    return c


def add_user(name, data):
    user = User.objects.create_user(name)
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.email = data["email"]
    u.age = data["age"]
    u.save()
    return u


if __name__ == '__main__':
    print('-Starting population script-')
    populate()
