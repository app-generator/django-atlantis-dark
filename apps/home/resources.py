from .models import apicase
from import_export import resources
from import_export.fields import Field
from .models import TesT

class TestResource(resources.ModelResource):

    sl_no = Field(attribute='sl_no',column_name='SL No')
    d_s = Field(attribute='d_s',column_name='Module*')
    pre_req = Field(attribute='pre_req',column_name='Prerequisite')
    t_scenario = Field(attribute='t_scenario',column_name='Test Scenario (With Steps)*')
    exp_result = Field(attribute='exp_result',column_name='Expected Result*')
    exp_plat = Field(attribute='exp_plat',column_name='Execution Platform*')
    a_exe = Field(attribute='a_exe',column_name='Execution priority*')
    b_status = Field(attribute='b_status',column_name='Test Status')
    c_date = Field(attribute='c_date',column_name='Execution Date')
    d_owner = Field(attribute='d_owner',column_name='Manual QA Owner')
    e_id = Field(attribute='e_id',column_name='Jira ID')
    f_auto = Field(attribute='f_auto',column_name='Automation Status')
    g_aown = Field(attribute='g_aown',column_name='Automation Owner')
    h_poc = Field(attribute='h_poc',column_name='Developer POC Product POC *')
    i_comm = Field(attribute='i_comm',column_name='Comments')
    class Meta:
        model = TesT


class ApiResource(resources.ModelResource):

    sl_no = Field(attribute='sl_no',column_name='SNo*')
    api_type = Field(attribute='api_type',column_name='API Type*')
    priority = Field(attribute='priority',column_name='Priority*')
    Dependencies = Field(attribute='Dependencies',column_name='Dependencies')
    Description = Field(attribute='Description',column_name='Description*')
    service_name = Field(attribute='service_name',column_name='Service Name*')
    owner_poc = Field(attribute='owner_poc',column_name='Owner POC*')
    mock_link = Field(attribute='mock_link',column_name='Mock Link*')
    curl = Field(attribute='curl',column_name='Curl*')
    dependent_services = Field(attribute='dependent_services',column_name='Dependent Services')
    dependent_spoc = Field(attribute='dependent_spoc',column_name='Dependent SPOC')
    dev_status = Field(attribute='dev_status',column_name='Dev Status*')
    open_q = Field(attribute='open_q',column_name='Open Questions')
    status = Field(attribute='status',column_name='Status*')
    test_owner = Field(attribute='test_owner',column_name='Test owner')
    jira = Field(attribute='jira',column_name='Jira')
    i_comm = Field(attribute='i_comm',column_name='Comments')
    class Meta:
        model = apicase