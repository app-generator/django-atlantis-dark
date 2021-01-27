from django.contrib import admin
from muhasebe.models import CariKart, CariGrup

@admin.register(CariKart)
class CariKartAdmin(admin.ModelAdmin):
    pass

@admin.register(CariGrup)
class CariGrupAdmin(admin.ModelAdmin):
    pass