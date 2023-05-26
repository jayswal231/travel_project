from django.db import models
from package.models import Package
# Create your models here.
class PackageEnquiry(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    number_of_persons = models.IntegerField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class ContactUs(models.Model):
    name = models.CharField(max_length=199)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=299, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name