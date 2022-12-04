from django.shortcuts import render
from .forms import quessionForm
from .models import Quession
# Create your views here.

def homepage(request):
    return render(request, 'FAQ/index.html')

def quessions(request):
    quessions = Quession.objects.all()
    succes = ''
    quessForm = quessionForm()
    if request.method == 'POST':
        quessForm = quessionForm(request.POST)
        if quessForm.is_valid():
            quession = Quession()
            quession.name = quessForm.cleaned_data['name']
            quession.email = quessForm.cleaned_data['email']
            quession.quession = quessForm.cleaned_data['quession']
            quession.save()
            succes = 'Successfull'
        else:
            succes = 'Ceva a mers prost'
    return render(request, 'FAQ/html/faq.html', {"form" : quessForm, 'quessions' : quessions, 'success' : succes})

def contact(request):
    return render(request, 'FAQ/html/contact.html')

def company(request):
    return render(request, 'FAQ/html/company.html')
