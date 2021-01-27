from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class CariGrup(models.Model):
    ad = models.CharField(max_length=50, verbose_name="ad")

    def __str__(self):
        return self.ad

class CariKart(models.Model):
    AKTIF_PASIF_CHOICES = [
        ('A', 'Aktif'),
        ('P', 'Pasif'),
    ]

    cari_kodu = models.CharField(max_length=30)
    ad = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    ilce = models.IntegerField()
    sehir = models.IntegerField()
    eposta = models.EmailField()
    web_adresi = models.CharField(max_length=200)
    aciklama = models.CharField(max_length=500)
    cari_grup = models.ForeignKey(CariGrup, verbose_name='carigrup', on_delete=None, blank=True, null=True)
    telefon_1 = PhoneNumberField(blank=True)
    telefon_2 = PhoneNumberField(blank=True)
    gsm_1 = PhoneNumberField(blank=True)
    gsm_2 = PhoneNumberField(blank=True)
    acik_hesap_limiti = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    vergi_dairesi = models.CharField(max_length=50, null=True)
    vergi_numarasi = models.IntegerField(null=True)
    tc_kimlik_numarasi = models.IntegerField(null=True)
    yetkili_adi = models.CharField(max_length=100, null=True)
    aktif_pasif = models.CharField(max_length=1, choices=AKTIF_PASIF_CHOICES, default='A')




    def __str__(self):
        return "(" + self.cari_kodu + ") " + self.ad if self.cari_kodu else self.ad

    def get_absolute_url(self):
        return reverse('muhasebe:cari_kart_guncelle', kwargs={'pk': self.pk})

    @property
    def cari(self):
        return "{} - {}".format(self.cari_kodu, self.ad)
