from django.db import models
from django.forms import forms
# Create your models here.
class contactForm(models.Model):
    cName= models.CharField(max_length=50)
    cMail= models.EmailField()
    cSub = models.CharField(max_length=200)
    cSms = models.CharField(max_length=5000)

    def __str__(self) :
        return self.cMail
