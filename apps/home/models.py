# -*- encoding: utf-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from dataclasses import Field
from logging import lastResort
from core import settings
from datetime import datetime as dtdt
import django.utils.formats as django_format
from django.utils import timezone
#from django.utils.translation import gettext as _
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from import_export.fields import Field

Rating = [
    ('b', 'Bad'),
    ('a', 'Average'),
    ('e', 'Excellent')
]
#DataFlair
class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    #img = models.ImageField(upload_to='pics')
    #mfg_date = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=1, choices=Rating)
    #file_up = models.FileField(upload_to='files/')
    def _str_(self):
        return self.name

    def show_desc(self):
        return self.description[:50]


class Device(models.Model):
    fn = models.CharField(max_length=100,db_column='Last*')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

class TesT(models.Model):

    sl_no = models.IntegerField(default=0,editable=True,null=True,blank=True)
    d_s = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    pre_req = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    t_scenario = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    exp_result = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class expl(models.TextChoices):
        API = 'api', _('api')
        ANDROID = 'android', _('android')
        WEB = 'web', _('web')
        PWA = 'pwa', _('pwa')
        IOS = 'ios', _('ios')
    exp_plat = models.CharField(max_length=500,choices=expl.choices,default='0',editable=True,null=True,blank=True)
    class aexe(models.TextChoices):
        p1 = 'p1', _('p1')
        p2 = 'p2', _('p2')
        p3 = 'p3', _('p3')

    a_exe = models.CharField(max_length=500,choices=expl.choices,default='0',editable=True,null=True,blank=True)
    class st(models.TextChoices):
        passed = 'passed', _('passed')
        failed = 'failed', _('failed')
        pending = 'pending', _('pending')
        blocked = 'blocked', _('blocked')
        NA = 'NA', _('NA')
    b_status = models.CharField(max_length=500,choices=st.choices,default='0',editable=True,null=True,blank=True)
    
    c_date = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class mo(models.TextChoices):
        H = 'Harish A', _('Harish A')
        Z = 'zilka mehta', _('zilka mehta')
    d_owner = models.CharField(max_length=500,choices=mo.choices,default='0',editable=True,null=True,blank=True)
    e_id = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class aut(models.TextChoices):
        pending = 'pending', _('pending')
        automated = 'automated', _('automated')
        automatable = 'automatable', _('automatable')
        failed = 'failed', _('failed')
        blocked = 'blocked', _('blocked')
        TBD = 'TBD', _('TBD')
        NA = 'NA', _('NA')
    f_auto = models.CharField(max_length=500,choices=aut.choices,default='0',editable=True,null=True,blank=True)
    g_aown = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class poc(models.TextChoices):
        H = 'Himanshu Nikhare', _('Himanshu Nikhare')
        R = 'Rakesh Kumar', _('Rakesh Kumar')
    h_poc = models.CharField(max_length=500,choices=poc.choices,default='0',editable=True,null=True,blank=True)
    i_comm = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
class TestSummary(TesT):
    class Meta:
        proxy = True
        verbose_name = "Test Summary"
        verbose_name_plural = "Tests Summary"

class apicase(models.Model):
    sl_no = models.IntegerField(default=0,editable=True,null=True,blank=True)
    api_type = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class p(models.TextChoices):
        p1 = 'p1', _('p1')
        p2 = 'p2', _('p2')
        p3 = 'p3', _('p3')
    priority = models.CharField(max_length=500,choices=p.choices,default='0',editable=True,null=True,blank=True)
    Dependencies = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    Description = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    service_name = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    owner_poc = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    mock_link = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    curl = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    dependent_services = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    dependent_spoc = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    class p(models.TextChoices):
        n = 'dev in progress', _('dev in progress')
        ps = 'tbd', _('tbd')
        pj = 'finished', _('finished')
    dev_status = models.CharField(max_length=500,choices=p.choices,default='0',editable=True,null=True,blank=True)
    open_q = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    

    class t(models.TextChoices):
        pending = 'pending', _('pending')
        automated = 'automated', _('automated')
        automatable = 'automatable', _('automatable')
        failed = 'failed', _('failed')
        blocked = 'blocked', _('blocked')
        TBD = 'TBD', _('TBD')
        NA = 'NA', _('NA')
    status = models.CharField(max_length=500,choices=t.choices,default='0',editable=True,null=True,blank=True)
    test_owner = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    jira = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)
    i_comm = models.CharField(max_length=500,default='0',editable=True,null=True,blank=True)