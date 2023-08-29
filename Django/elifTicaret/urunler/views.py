from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    urunler = Urun.objects.all()

    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(isim__icontains = search)

    context = {
        'urunlerim': urunler,
        'search': search
    }
    return render(request, 'index.html', context)

def urun(request, urunId):
    urun = Urun.objects.filter(id = urunId)

    context = {
        'urun': urun
    }
    return render(request, 'urun.html', context)

def olustur(request):
    if request.method == 'POST':
        resim = request.FILES['resim']
        isim = request.POST['isim']
        aciklama = request.POST['aciklama']
        fiyat = request.POST['fiyat']

        urun = Urun.objects.create(
            isim = isim,
            aciklama = aciklama,
            resim = resim,
            fiyat = fiyat
        )
        urun.save()
        print("Ürün OLuşturuldu")
        return redirect('olustur')
    return render(request, 'olustur.html')
