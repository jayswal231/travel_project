from django.db import models

# Create your models here.
class AboutCompany(models.Model):
    company_name = models.CharField(max_length=199)
    company_profile = models.ImageField(upload_to='media',null=True, blank=True)
    about_company = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=199,null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=199)
    company_profile = models.ImageField( upload_to='media',null=True, blank=True)
    about_company = models.TextField(null=True, blank=True)
    company_history = models.TextField(null=True, blank=True)
    company_missions = models.TextField(null=True, blank=True)
    your_value = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.company_name
    

class TermsConditions(models.Model):
    terms_conditions = models.TextField()

class PrivacyAndPolicy(models.Model):
    privacy_and_policy = models.TextField()
