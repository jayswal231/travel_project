from django.urls import path
from .views import *

urlpatterns = [
    # PackageEnquiry
    path('contact/enquiry-list/',PackageEnquiryListView.as_view(), name='enquiry-list' ),
    path('contact/enquiry-create/',PackageEnquiryCreateView.as_view(), name='enquiry-create' ),
    path('contact/enquiry-update/<int:pk>/', PackageEnquiryUpdateView.as_view(), name='enquiry-update'),
    path('contact/enquiry-delete/',PackageEnquiryDeleteView.as_view(), name='enquiry-delete' ),

    # ContactUs
    path('contact/contact-list/',ContactUsListView.as_view(), name='contact-list' ),
    path('contact/contact-create/',ContactUsCreateView.as_view(), name='contact-create' ),
    path('contact/contact-update/<int:pk>/',ContactUsUpdateView.as_view(), name='contact-update' ),
    path('contact/contact-delete/',ContactUsDeleteView.as_view(), name='contact-delete' ),


]