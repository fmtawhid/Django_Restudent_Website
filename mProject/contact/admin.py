from django.contrib import admin
from contact.models import contactForm
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display=('cName','cMail','cSub','cSms')
admin.site.register(contactForm, contactAdmin)