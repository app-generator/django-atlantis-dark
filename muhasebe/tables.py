import django_tables2 as tables

from .models import CariKart
import itertools
from django.utils.html import format_html
from django_tables2.utils import A

class CariKartColumn(tables.Column):
    def render(self, value, record):
        return "{} - {}".format(record.cari_kodu, record.ad)

class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return "Toplam: {}".format(
            sum(bound_column.accessor.resolve(row) for row in table.data)
        )

class CountingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return "Adet: {}".format(
            len(table.data)
        )


class CariKartTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        model = CariKart
        fields = ["cari_kodu", "ad", "eposta", "web_adresi", "yetkili_adi"]
        sequence = ('selection', "edit", "cari_kodu", "ad", "eposta", "web_adresi", "yetkili_adi")
        attrs = {"class": "display table table-striped table-hover"}
    
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    #ad = CariKartColumn(verbose_name="Cari")
    ln = tables.Column(accessor="vergi_numarasi")
    region_name = tables.Column(accessor="cari_grup__ad")
    acik_hesap_limiti = SummingColumn()
    ad = CountingColumn()
    edit = tables.LinkColumn('muhasebe:cari_kart_guncelle', args=[A('pk')], orderable=False, empty_values=())

    def render_edit(self):
        return "Gör"


    #def render_ad(self, value):
    #    return value + ".."

    #def render_ad(self, value, record):
    #    return format_html("<b>{} {}</b>", value, record.eposta)


