from django.contrib import admin
from ClubScoutGlasgow.models import UserProfile, Club
# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Club, ClubAdmin)

admin.site.register(UserProfile)
