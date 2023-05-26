from django.urls import path
from .views import *

urlpatterns = [
    # AboutCompany
    path('website/about-company/list/', AboutCompanyListView, name='about-company-list'),
    path('website/about-company/update/<int:pk>/', AboutCompanyUpdateView.as_view(), name='about-company-update'),

   # CompanyProfile
    path('website/company-profile/list/', CompanyProfileListView, name='company-profile-list'),
    path('website/company-profile/update/<int:pk>/', CompanyProfileUpdateView.as_view(), name='company-profile-update'),
   
   # TermsConditions
    path('terms-conditions/list/', TermsConditionsListView.as_view(), name='terms-conditions-list'),
    path('terms-conditions/create/', TermsConditionsCreateView.as_view(), name='terms-conditions-create'),
    path('terms-conditions/update/<int:pk>/', TermsConditionsUpdateView.as_view(), name='terms-conditions-update'),
    path('terms-conditions/delete/<int:pk>/', TermsConditionsDeleteView.as_view(), name='terms-conditions-delete'),

   # PrivacyAndPolicyListView
    path('policy/list/', PrivacyAndPolicyListView.as_view(), name='policy-list'),
    path('policy/create/', PrivacyAndPolicyCreateView.as_view(), name='policy-create'),
    path('policy/update/<int:pk>/', PrivacyAndPolicyUpdateView.as_view(), name='policy-update'),
    path('policy/delete/<int:pk>/', PrivacyAndPolicyDeleteView.as_view(), name='policy-delete'),

]
