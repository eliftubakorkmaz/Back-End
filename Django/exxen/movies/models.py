from django.db import models

# Create your models here.
class Movie(models.Model):
    isim = models.CharField(max_length=50)
    resim = models.FileField(upload_to='filmler/', verbose_name='Film Resmi')

    def __str__(self):
        return self.isim    