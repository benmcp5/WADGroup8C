from django.contrib import admin
from ClubScoutGlasgow.models import UserProfile, Club, ClubImage, Review
# Register your models here.

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    inlines = [ClubImageInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewID', 'reviewer', 'club','reviewDate')


admin.site.register(Club, ClubAdmin)

admin.site.register(UserProfile)

admin.site.register(Review, ReviewAdmin)
