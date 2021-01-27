from django.urls import path
from . import views
from django_filters.views import FilterView
from .models import CariKart

app_name = "muhasebe"

urlpatterns = [
    path('cari_kart/', views.CariKartListView.as_view(), name="cari_kart"),
    path('cari_kart/ekle/', views.CariKartCreateView.as_view(), name="cari_kart_ekle"),
    path('cari_kart/<int:pk>/guncelle/', views.CariKartUpdateView.as_view(), name="cari_kart_guncelle"),
    path('cari_kart/<int:pk>', views.CariKartDetailView.as_view(), name='cari_kart_detay'),
    
]