# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product
from .models import Device
from .resources import *
from .models import TesT,TestSummary,apicase
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce
from django.db.models import FloatField, F
from django.db.models.functions import Cast
from django.db.models import Count,IntegerField
    #ordering = ('sl_no',)
# Register your models here.
# DataFlair
# ModelAdmin Class # DataFlair

def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')
    change_rating.short_description = "Mark Selected Products as Excellent"
class ProductA(ImportExportModelAdmin,admin.ModelAdmin):
    #exclude = ('description', )
    list_display = ('name','description','rating')
    list_filter = ('name','rating')
    actions = [change_rating]
class DeviceA(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('fn','first_name','last_name','company_name','address','city','country','postal','phone','email','web')
    list_filter = ('first_name','last_name','company_name','address','city','country','postal','phone','email','web')
    search_field = ('first_name','last_name','company_name','address','city','country','postal','phone','email','web')
    
class TestA(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sl_no','d_s','pre_req','t_scenario','exp_result','exp_plat','a_exe','b_status','c_date','d_owner','e_id','f_auto','g_aown','h_poc','i_comm')
    # list_display = ('sl_no','d_s')
    
    search_fields = ('sl_no','d_s','pre_req','t_scenario','exp_result','exp_plat','a_exe','b_status','c_date','d_owner','e_id','f_auto','g_aown','h_poc','i_comm')
    resource_class = TestResource
    ordering = ('sl_no',)

class apiA(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('sl_no','api_type','priority','Dependencies','Description','service_name','owner_poc','mock_link','curl','dependent_services','dependent_spoc','dev_status','open_q','status','test_owner','jira','i_comm')
    # list_display = ('sl_no','d_s')
    
    search_fields = ('sl_no','api_type','priority','Dependencies','Description','service_name','owner_poc','mock_link','curl','dependent_services','dependent_spoc','dev_status','open_q','status','test_owner','jira','i_comm')
    resource_class = ApiResource
    ordering = ('sl_no',)
admin.site.register(TesT,TestA)
@admin.register(TestSummary)
class TestSummaryAdmin(admin.ModelAdmin):
    search_fields=('exp_plat','f_auto')
    change_list_template = 'admin/test_summary_change_list.html'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        metrics = {
             'total': Count('sl_no'),
        #     'total_sales' : Count('exp_plat'),
            
        }
        response.context_data['summary'] = list(
            qs
            .values('exp_plat')
            .annotate(**metrics)
            .order_by('exp_plat')
        )
        response.context_data['automation_total']=list(
            qs.values('f_auto').annotate(**metrics).order_by('f_auto')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response
admin.site.register(Product,ProductA)
admin.site.register(Device,DeviceA)
admin.site.register(apicase,apiA)
admin.site.site_header = "BigBasket Testing admin"
