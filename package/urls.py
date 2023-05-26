from django.urls import path
from .views import *
urlpatterns = [
    # Itinerary
    path('package/itinerary-list/',ItineraryListView.as_view(), name='itinerary-list' ),
    path('package/itinerary-create/',ItineraryCreateView.as_view(), name='itinerary-create' ),
    path('package/itinerary-update/<int:pk>/',ItineraryUpdateView.as_view(), name='itinerary-update' ),
    path('package/itinerary-delete/<int:pk>/',ItineraryDeleteView.as_view(), name='itinerary-delete' ),

    # TripGrade
    path('package/tripgrade-create/',TripGradeCreateView.as_view(), name='tripgrade-create' ),
    path('package/tripgrade-delete/<int:pk>/',TripGradeDeleteView.as_view(), name='tripgrade-delete' ),

    # Package
    path('package/package-list/',PackageListView.as_view(), name='package-list' ),
    path('package/package-create/',PackageCreateView.as_view(), name='package-create' ),
    path('package/package-update/<int:pk>/',PackageUpdateView.as_view(), name='package-update' ),
    path('package/package-delete/<int:pk>/',PackageDeleteView.as_view(), name='package-delete' ),

    path('package/single-list/<int:pk>/',SinglePackageList.as_view(), name='single-list' ),


    # FrequentlyAskedQuestions
    path('package/questions-list/',FrequentlyAskedQuestionsListView.as_view(), name='questions-list' ),
    path('package/questions-create/',FrequentlyAskedQuestionsCreateView.as_view(), name='questions-create' ),
    path('package/questions-update/<int:pk>/',FrequentlyAskedQuestionsUpdateView.as_view(), name='questions-update' ),
    path('package/questions-delete/<int:pk>/',FrequentlyAskedQuestionsDeleteView.as_view(), name='questions-delete' ),


]