from .models import CariKart
import django_filters
from django_filters import ChoiceFilter
from .models import CariKart

class CariKartFilter(django_filters.FilterSet):
    class Meta:
        aktif_pasif = ChoiceFilter(choices = CariKart.AKTIF_PASIF_CHOICES)
        model = CariKart
        fields = {'ad': ['icontains'], 'aktif_pasif': ['exact']}
        

