from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
# Create your views here.

# Itinerary
class ItineraryListView(ListView):
    model = Itinerary
    template_name = 'package/itinerary_list.html'

class ItineraryCreateView(CreateView):
    model = Itinerary
    template_name = 'package/itinerary_create.html'
    fields = ['package','title', 'descriptions', 'trek_distance', 'highest_altitude', 'trek_durations', 'meals']
    success_url = '/package/itinerary-list/'

class ItineraryUpdateView(UpdateView):
    model = Itinerary
    template_name = 'package/itinerary_update.html'
    fields = ['title', 'descriptions', 'trek_distance', 'highest_altitude', 'trek_durations', 'meals']
    success_url = '/package/itinerary-list'
    pk_url_kwarg = 'pk'

class ItineraryDeleteView(DeleteView):
    model = Itinerary
    template_name = 'package/itinerary_delete.html'
    success_url = '/package/itinerary-list'
    pk_url_kwarg = 'pk'


# TripGrade
class TripGradeCreateView(CreateView):
    model = TripGrade
    template_name = 'package/trip_grade_create.html'
    fields = ['name']
    success_url = '/package/tripgrade-create/'

class TripGradeDeleteView(DeleteView):
    model = TripGrade
    template_name = 'package/trip_grade_create.html'
    success_url = '/package/tripgrade-create/'
    pk_url_kwarg = 'pk'

# Package
class PackageListView(ListView):
    model = Package
    template_name = 'package/package_list.html'

class PackageCreateView(CreateView):
    model = Package
    template_name = 'package/package_create.html'
    fields = ['name', 'price', 'discount_price', 'trip_durations', 'trip_grade', 'highest_altitude', 'accommodation',
               'group_size', 'best_season', 'brief_insight', 'highlights', 'itinerary', 'includes','excludes',
                 'trip_map', 'benefits', 'comprehensive_guide', 'packing_list', 'frequently_asked_questions']
    success_url  = '/package/package-list/'



class PackageUpdateView(UpdateView):
    model = Package
    template_name = 'package/package_update.html'
    fields = ['name', 'price', 'discount_price', 'trip_durations', 'trip_grade', 'highest_altitude', 'accommodation',
               'group_size', 'best_season', 'brief_insight', 'highlights', 'itinerary', 'includes','excludes',
                 'trip_map', 'benefits', 'comprehensive_guide', 'packing_list', 'frequently_asked_questions']
    success_url  = '/package/package-list/'
    pk_url_kwarg = 'pk'


class PackageDeleteView(DeleteView):
    model = Package
    template_name = 'package/package_delete.html'
    success_url = reverse_lazy('package-list')

class SinglePackageList(DetailView):
    model = Package
    template_name = 'package/single_package_list.html'
    # context_object_name = 'object'
    # page_kwarg = 'pk'


# FrequentlyAskedQuestions
class FrequentlyAskedQuestionsListView(ListView):
    model = FrequentlyAskedQuestions
    template_name = 'package/questions_list.html'
   

class FrequentlyAskedQuestionsCreateView(CreateView):
    model = FrequentlyAskedQuestions
    template_name = 'package/questions_create.html'
    fields = ['package', 'question', 'answer']
    success_url='/package/questions-list/'
    
   

class FrequentlyAskedQuestionsUpdateView(UpdateView):
    model = FrequentlyAskedQuestions
    template_name = 'package/home.html'

class FrequentlyAskedQuestionsDeleteView(DeleteView):
    model =  FrequentlyAskedQuestions
    template_name = 'package/home.html'
