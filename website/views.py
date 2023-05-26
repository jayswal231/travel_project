from django.shortcuts import render
from .models import *
from contact.models import ContactUs
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

# AboutCompany
def AboutCompanyListView(request):
    context = {}
    template_path = "website/about_company_list.html"
    context["object_list"] = [AboutCompany.objects.first()]
    return render(request, template_path, context)

class AboutCompanyUpdateView(UpdateView):
    model = AboutCompany
    template_name = 'website/about_company_create.html'
    fields = ['company_name', 'company_profile', 'about_company', 'title', 'descriptions']
    success_url = '/website/about-company/list/'
    pk_url_kwarg= 'pk'




# CompanyProfile
def CompanyProfileListView(request):
    context = {}
    template_path = "website/company_profile.html"
    context["object_list"] = [CompanyProfile.objects.first()]
    return render(request, template_path, context)
    

class CompanyProfileUpdateView(UpdateView):
    model = CompanyProfile
    template_name = 'website/company_profile_create.html'
    success_url = '/website/company-profile/list/'
    fields = ['company_name', 'company_profile', 'about_company', 'company_history', 'company_missions', 'your_value']
    pk_url_kwarg = 'pk'






# TermsConditions
class TermsConditionsListView(ListView):
    model = TermsConditions
    template_name = 'website/terms_conditions_list.html'

class TermsConditionsCreateView(CreateView):
    model = TermsConditions
    template_name = 'website/terms_conditions_create.html'
    fields = ['terms_conditions']
    success_url = '/terms-conditions/list/'


class TermsConditionsUpdateView(UpdateView):
    model = TermsConditions
    template_name = 'website/terms_conditions_create.html'
    fields = ['terms_conditions']
    success_url = '/terms-conditions/list/'
    pk_url_kwarg = 'pk'



class TermsConditionsDeleteView(DeleteView):
    model = TermsConditions
    template_name = 'website/terms_conditions_create.html'
    fields = ['terms_conditions']
    success_url = '/terms-conditions/list/'
    pk_url_kwarg = 'pk'


# PrivacyAndPolicy
class PrivacyAndPolicyListView(ListView):
    model = PrivacyAndPolicy
    template_name = 'website/policy_list.html'

class PrivacyAndPolicyCreateView(CreateView):
    model = PrivacyAndPolicy
    template_name = 'website/policy_create.html'
    fields = ['privacy_and_policy']
    success_url = '/policy/list/'
    

class PrivacyAndPolicyUpdateView(UpdateView):
    model = PrivacyAndPolicy
    template_name = 'website/policy_create.html'
    fields = ['privacy_and_policy']
    success_url = '/policy/list/'
    pk_url_kwarg = 'pk'

class PrivacyAndPolicyDeleteView(DeleteView):
    model = PrivacyAndPolicy
    template_name = 'website/policy_create.html'
    fields = ['privacy_and_policy']
    success_url = '/policy/list/'
    pk_url_kwarg = 'pk'