from django.contrib import admin
from pages.models import AddBook
# Register your models here.
class bookingAdmin(admin.ModelAdmin):
    list_display=('Bname','Bmail','Bdate','Bnop','Btext')
admin.site.register(AddBook, bookingAdmin)
