from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            subject = '17 Ocak sınıfının son demleri'
            message = 'Bu eğitimi 17 Ocak sınıfı ile yaptık'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [form.email]
            )
            return redirect('login')
        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if kullanici is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('index')