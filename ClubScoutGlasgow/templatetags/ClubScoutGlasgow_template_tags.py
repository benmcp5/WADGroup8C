from django import template
from ClubScoutGlasgow.models import Club
register=template.Library()

@register.inclusion_tag('ClubScoutGlasgow/clubs.html')
def get_club_list(current_club=None):
    return {'clubs': Club.objects.all(), 'current_club':current_club}
