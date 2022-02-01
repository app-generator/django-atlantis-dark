# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import pandas as pd
from django.shortcuts import render,redirect
from .models import TesT,apicase
from testvault import settings
from sqlalchemy import create_engine
#def hello_world(request):
#    return render(request, 'hello_world.html', {})
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    tests = TesT.objects.all()
    return render(request,'home/index.html',{'tests' : tests})
@login_required(login_url="/login/")    
def tables(request):
    tests = TesT.objects.all()
    return render(request,'home/tables-data.html',{'tests' : tests})
@login_required(login_url="/login/")    
def apitables(request):
    apis = apicase.objects.all()
    return render(request,'home/tables-api.html',{'apis' : apis})
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
class UploadFileForm(forms.Form):
    file = forms.FileField()

def store(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            xls = pd.ExcelFile(request.FILES['file'])
            for sheet in xls.sheet_names:
                print(sheet)
                if(sheet!='Summary'):
                    df = pd.read_excel(xls,sheet,header=9)
                    if(df.empty):
                        continue
                    else:
                        if('API' in sheet):
                            df.columns = ['sl_no','api_type','priority','Dependencies','Description','service_name','owner_poc','mock_link','curl','dependent_services','dependent_spoc','dev_status','open_q','status','test_owner','jira','i_comm']
                            user = settings.DATABASES['default']['USER']
                            password = settings.DATABASES['default']['PASSWORD']
                            database_name = settings.DATABASES['default']['NAME']
                            database_url = 'mysql://{user}:{password}@localhost/{database_name}'.format(
                            user=user,
                            password=password,
                            database_name=database_name,
                            )
                            engine = create_engine(database_url, echo=False)
                            df.to_sql('home_apicase', con=engine,  if_exists='append', chunksize = 1000, index= False)
                        else:
                            df.columns = ['sl_no','d_s','pre_req','t_scenario','exp_result','exp_plat','a_exe','b_status','c_date','d_owner','e_id','f_auto','g_aown','h_poc','i_comm']
                            user = settings.DATABASES['default']['USER']
                            password = settings.DATABASES['default']['PASSWORD']
                            database_name = settings.DATABASES['default']['NAME']
                            database_url = 'mysql://{user}:{password}@localhost/{database_name}'.format(
                            user=user,
                            password=password,
                            database_name=database_name,
                            )
                            engine = create_engine(database_url, echo=False)
                            df.to_sql('home_test', con=engine,  if_exists='append',chunksize = 1000, index= False)
            # df2.save_to_database(
            #     model=[apicase],
            #     mapdict=['sl_no','api_type','priority','Dependencies','Description','service_name','owner_poc','mock_link','curl','dependent_services','dependent_spoc','dev_status','open_q','status','test_owner','jira','i_comm']
            # )
            # df3.save_to_database(
            #     model = [TesT],
            #     mapdict=['sl_no','d_s','pre_req','t_scenario','exp_result','exp_plat','a_exe','b_status','c_date','d_owner','e_id','f_auto','i_comm']
            # )
            # request.FILES['file'].save_book_to_database(
            #     model=[apicase,TesT],
            #     initializers = [10,10],
            #     mapdict=[['sl_no','api_type','priority','Dependencies','Description','service_name','owner_poc','mock_link','curl','dependent_services','dependent_spoc','dev_status','open_q','status','test_owner','jira','i_comm'],['sl_no','d_s','pre_req','t_scenario','exp_result','exp_plat','a_exe','b_status','c_date','d_owner','e_id','f_auto','i_comm']]
            #     )
            # return HttpResponse("OK")
            return redirect('home/index.html')
        else:
            return HttpResponseBadRequest()
    else:
        return render(request, 'home/excfile.html', {})