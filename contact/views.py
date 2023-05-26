from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import *
# Create your views here.

# PackageEnquiry
class PackageEnquiryListView(ListView):
    model = PackageEnquiry
    template_name = 'contact/enquirylist.html'

class PackageEnquiryCreateView(CreateView):
    model = PackageEnquiry
    template_name = 'contact/enquirycreate.html'
    fields = ['package', 'name', 'email', 'phone', 'message', 'number_of_persons', 'date']
    success_url = '/travel/contact/enquiry-list/'
    
    
class PackageEnquiryUpdateView(UpdateView):
    model = PackageEnquiry
    template_name = 'contact/enquiry_update.html'
    fields = ['package', 'name', 'email', 'phone', 'message', 'number_of_persons', 'date']
    pk_url_kwarg = 'pk'
    success_url = '/travel/contact/enquiry-list/'
    

class PackageEnquiryDeleteView(DeleteView):
    model = PackageEnquiry
    template_name = 'contact/home.html'


# ContactUs
class ContactUsListView(ListView):
    model = ContactUs
    template_name = 'contact/home.html'

class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contact/home.html'

class ContactUsUpdateView(UpdateView):
    model = ContactUs
    template_name = 'contact/home.html'

class ContactUsDeleteView(DeleteView):
    model = ContactUs
    template_name = 'contact/home.html'
