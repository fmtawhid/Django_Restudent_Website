from django.shortcuts import render
from contact.models import contactForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['nam']
        mail = request.POST['mail']
        sub = request.POST['sub']
        sms = request.POST['sms']
    
        cView = contactForm(cName=name, cMail=mail, cSub=sub, cSms=sms)
        cView.save()

    return render(request, 'contact/contact.html')
