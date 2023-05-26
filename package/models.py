from django.db import models
import uuid
# Create your models here.


class TripGrade(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Package(models.Model):
    name = models.CharField(max_length=299)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    trip_durations = models.CharField(max_length=100)
    trip_grade = models.ForeignKey(TripGrade, on_delete=models.CASCADE)
    highest_altitude = models.FloatField(null=True, blank=True)
    accommodation = models.CharField(max_length=299, null=True, blank=True)
    group_size = models.CharField(max_length=100, null=True, blank=True)
    best_season = models.CharField(max_length=299, null=True, blank=True)
    brief_insight = models.TextField(null=True, blank=True)
    highlights = models.TextField(null=True, blank=True)
    itinerary = models.CharField(max_length=299)
    includes = models.TextField(null=True, blank=True)
    excludes = models.TextField(null=True, blank=True)
    trip_map = models.ImageField(upload_to='media',null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    comprehensive_guide = models.TextField(null=True, blank=True)
    packing_list = models.TextField()
    frequently_asked_questions = models.CharField(max_length=599, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Itinerary(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='itineraries')
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    trek_distance = models.FloatField(null=True, blank=True)
    highest_altitude = models.FloatField(null=True, blank=True)
    trek_durations = models.CharField(max_length=100)
    meals = models.CharField(max_length=299)

    def __str__(self):
        return self.title
    
    

class FrequentlyAskedQuestions(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    question = models.CharField(max_length=299, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question

    
