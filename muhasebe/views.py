from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import CariKart, CariGrup
from django.forms import ModelForm, Textarea
from django import forms
from .forms import CariKartCreateFrom, CariKartUpdateFrom
from django_tables2 import SingleTableView, LazyPaginator
from .tables import CariKartTable
from django_filters.views import FilterView
from .filters import CariKartFilter
from django_tables2.export.views import ExportMixin

'''
def CariKartListView(request):
    cariKartlar = CariKart.objects.all()
    filter = CariKartFilter(request.GET, queryset = cariKartlar)
    table = CariKartTable(filter.qs)
    return render(request, "muhasebe/carikart_list.html", {
        "table": table, 'filter' : filter
    })
'''

class CariKartListView(ExportMixin, FilterView, SingleTableView):
    model = CariKart
    template_name = "muhasebe/carikart_list.html"
    table_class = CariKartTable
    
    table_pagination = {
        "per_page": 5
    }
    
    filterset_class = CariKartFilter

    exclude_columns = ('buttons', 'edit')



    
    #table_data = CariKart.objects.all()
    #paginator_class = LazyPaginator

class CariKartCreateView(CreateView):
    model = CariKart
    form_class = CariKartCreateFrom


class CariKartUpdateView(UpdateView):
    model = CariKart
    form_class = CariKartUpdateFrom

class CariKartDetailView(DetailView):
    queryset = CariKart.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj