from django.shortcuts import render
from pages.models import AddBook
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        date = request.POST['date']
        nop = request.POST['nop']
        text = request.POST['text']

        newBook =AddBook(Bname = name, Bmail = mail, Bdate = date, Bnop =nop, Btext=text)
        newBook.save()
    return render(request, 'home/index.html')
