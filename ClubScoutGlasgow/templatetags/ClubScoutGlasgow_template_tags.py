from django import template
from ClubScoutGlasgow.models import Club
register=template.Library()

@register.inclusion_tag('ClubScoutGlasgow/clubs.html')
def get_club_list(current_club=None):
    return {'clubs': Club.objects.all(), 'current_club':current_club}

@register.inclusion_tag('ClubScoutGlasgow/club.html')
def get_image_url(images):
    urls = {}
    i = 0;
    for image in images:
        urls[i] = image
        i+=1

    return urls