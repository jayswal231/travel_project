from django.contrib import admin
from .models import *
# Register your models here.
model = [Itinerary, TripGrade, Package, FrequentlyAskedQuestions]

admin.site.register(model)