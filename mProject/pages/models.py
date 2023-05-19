from django.db import models 

# Create your models here.
class AddBook(models.Model):
    Bname = models.CharField(max_length=40)
    Bmail = models.EmailField()
    Bdate = models.CharField(max_length=100)
    Bnop = models.IntegerField()
    Btext = models.CharField(max_length=500)

    def __str__(self) :
        return self.Bmail