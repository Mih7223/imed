from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm

def home_view(request):
    #return HttpResponse('AHLA IMED')
    return render(request, 'home.html')

def contact_view(request):
    #return HttpResponse('contactez-nous')
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            titre = f'Blog | {nom} {prenom} - {email}'

            send_mail(titre, message, 'aminatoomi@gmail.com',
                      ['aminatoomi@gmail.com'])

        return HttpResponseRedirect(reverse('remerciements'))
    return render(request, 'contact.html',context={'form': form})

def remerciements_view(request):
    return HttpResponse("merci d'avoir nous contacter")

