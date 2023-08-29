from django.db import models

# Create your models here.

class Urun(models.Model):
    resim = models.FileField(upload_to='urunler/', null=True, blank=True)
    isim = models.CharField(max_length=200)
    aciklama = models.TextField(max_length=400)
    fiyat = models.IntegerField()

    def __str__(self):
        return self.isim