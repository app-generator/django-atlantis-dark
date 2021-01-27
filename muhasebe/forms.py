from django.forms import ModelForm
from django.forms import Textarea

from .models import CariKart

class CariKartCreateFrom(ModelForm):
    class Meta:
        model = CariKart
        fields = "__all__"
        widgets = {
            "aciklama": Textarea(
                attrs={
                    'rows':4, 'cols':40
                }
            )
        }

class CariKartUpdateFrom(ModelForm):
    class Meta:
        model = CariKart
        fields = "__all__"
        widgets = {
            "aciklama": Textarea(
                attrs={
                    'rows':4, 'cols':40
                }
            )
        }