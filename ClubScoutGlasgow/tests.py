from django.test import TestCase

# Create your tests here.

from ClubScoutGlasgow import Users, Reviews, Clubs

class Clubs(TestCase):
    def test_ensure_all_number_fields_are_positive(self):

        club = Club("Club", -5, "Glasgow", -1, "10-10", 3.6, "www.google.com", "www.instagram.com", "www.facebook.com", )
        club.save()

        self.assertEqual((club.entryPrice>=0), True)
        self.assertEqual((club.noOfRooms>=0), True)
        self.assertEqual((club.averageOverallRating>=0), True)

    def test_ensure_all_number_fields_are_positive(self):
        club = Club("Club", -5, "Glasgow", -1, "10-10", 3.6, "www.google.com", "www.instagram.com", "www.facebook.com")
        club.save()

        
