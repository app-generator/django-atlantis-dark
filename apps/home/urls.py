# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path("tables/",views.tables,name='tables'),
    path("apitables",views.apitables,name='apitables'),
    path("store/",views.store,name='store'),
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    # Matches any html file
    
]
