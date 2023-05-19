from django.shortcuts import render
from .models import AddBook
# Create your views here.
def page1(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        date = request.POST['date']
        nop = request.POST['nop']
        text = request.POST['text']

        newBook =AddBook(Bname = name, Bmail = mail, Bdate = date, Bnop =nop, Btext=text)
        newBook.save()

    return render(request, 'pages/booking.html')
def page2(request):
    return render(request, 'pages/team.html')
def page3(request):
    return render(request, 'pages/testimonial.html')
