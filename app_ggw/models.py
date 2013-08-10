from django.db import models

# Create your models here.
class User(models.Model):

	facebook_id = models.BigIntegerField()
	name = models.CharField(max_length=100)
	email = models.EmailField(primary_key=True)
	graduate_time = models.DateField(blank=True)

	def __unicode__(self):
		return self.email


class City(models.Model):
	city_name = models.CharField(max_length=100)
	country_name = models.CharField(max_length=100)

	class Meta:
		unique_together= (('city_name', 'country_name'),)

	def __unicode__(self):
		return self.city_name + '[' + self.country_name + ']'


class Trip(models.Model):
	user_id = models.ForeignKey(User)
	place_1 = models.ForeignKey(City, unique=True, related_name='place_1')
	place_2 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_2')
	place_3 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_3')
	place_4 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_4')
	place_5 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_5')
	place_6 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_6')
	place_7 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_7')
	place_8 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_8')
	place_9 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_9')
	place_10 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_10')
	place_11 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_11')
	place_12 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_12')
	place_13 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_13')
	place_14 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_14')
	place_15 = models.ForeignKey(City, unique=True, blank=True, null=True, related_name='place_15')

	def __unicode__(self):
		return self.user_id + '[' + self.place_1 + ', ...]'


		