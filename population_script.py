import os

import django

# from ClubScoutGlasgow.models import Club, Review

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WADGroup8C.settings')

# NOT OPERATIONAL

django.setup()


def populate():

    """
    template

    "" : {
            "location": "",
            "openingHours": "",
            "website": "",
            "instagram": "",
            "facebook": "",
            "about": "",
        }

    """

    clubs = {
        "Sub Club" : {
            "location" : "22 Jamaica Street",
            "openingHours" : "23:00-3:00",
            "website" : "https://subclub.co.uk/",
            "instagram" : "https://www.instagram.com/subclub87/",
            "facebook" : "https://www.facebook.com/subclub",
            "about" : "The Sub Club is a club and music venue located at 22 Jamaica Street in Glasgow, Scotland."
                      " It opened 1 April 1987 and is the longest running underground dance club in the world."
                      " The 3,500-square-foot (330 m2) basement space can legally hold up to 410 people."
                      " In 2008 it was voted the 10th best club in the world by Resident Advisor (and 5th "
                      "for atmosphere) and the 30th best club in the world by DJ Mag. In 2009 the club was placed"
                      " 14th best in the world by DJ Mag.",
        },
        "The Garage" : {
            "location": "490 Sauchiehall St",
            "openingHours": "23:00-3:00",
            "website": "https://garageglasgow.co.uk/",
            "instagram": "https://www.instagram.com/thegarageglasgow/",
            "facebook": "https://www.facebook.com/garageglasgow/",
            "about": "The Garage (formerly known as The Mayfair) is a music venue and nightclub located at 490 "
                     "Sauchiehall Street in Glasgow, Scotland. It is Scotland's largest nightclub. The main "
                     "hall was the first Locarno ballroom in the UK, although it has since been remodelled by "
                     "the addition of an extension to the mezzanine level. The Garage is made up of various rooms "
                     "which play different genres of music which are all accessed under one roof. The Main hall, "
                     "the biggest room, plays chart and remixes, G2 plays RnB hits, Desperados bar plays cheesy "
                     "and nostalgia while the final room The Attic plays indie and rock. There is also a shot and "
                     "cocktail bar at the back of Desperados bar. ",
        },
        "Nice \'N\' Sleazy" : {
            "location": "421 Sauchiehall St, Glasgow G2 3LG",
            "openingHours": "18:00-3:00",
            "website": "https://www.nicensleazy.com/",
            "instagram": "https://www.instagram.com/nicensleazy/",
            "facebook": "https://www.facebook.com/nicensleazyglasgow/",
            "about": "Buzzing bar with poster plastered walls and small capacity creating atmospheric musical "
                     "intimacy.",
        },
        "SWG3" : {
            "location": "100 Eastvale Pl, Stobcross Rd, Glasgow G3 8QG",
            "openingHours": "10:00-18:00",
            "website": "https://swg3.tv/",
            "instagram": "https://www.instagram.com/swg3glasgow/",
            "facebook": "https://www.facebook.com/SWG3glasgow/",
            "about": "SWG3 (Studio Warehouse Glasgow) is a multi-disciplinary arts space in the westend of Glasgow. "
                     "We run an annual programme of exhibitions, band nights and events as well as being home to a "
                     "community of over 120 artists and musicians.",
        }
    }

    """
    for i in clubs["Sub Club"]:
        print(clubs["Sub Club"][i])
    """

if __name__ == '__main__':
    print('-Starting population script-')
    populate()
