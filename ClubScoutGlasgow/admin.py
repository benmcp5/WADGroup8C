from django.contrib import admin
from ClubScoutGlasgow.models import UserProfile, Club, ClubImage
# Register your models here.

class ClubImageInline(admin.TabularInline):
    model = ClubImage


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    inlines = [ClubImageInline]



admin.site.register(Club, ClubAdmin)

admin.site.register(UserProfile)
