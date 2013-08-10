from django.contrib import admin
from ggw.models import User, City, Trip

class CitiesInLine(admin.StackedInline):
    model = City
    extra = 3

class TripsInLine(admin.StackedInline):
    model = Trip
    extra = 3
    inlines = [CitiesInLine]

class UserAdmin(admin.ModelAdmin):
	fields = ['facebook_id', 'name', 'email', 'graduate_time']
	inlines = [TripsInLine]

admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Trip)