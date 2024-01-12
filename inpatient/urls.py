from . import views 
from django.conf.urls import url
from django.urls import include, re_path, path
from inpatient.views import AdmitView, AdmissionsView, AdmissiondetailView
from . import views 

app_name = 'inpatient'

urlpatterns = [
    re_path('admitpatient/', AdmitView.as_view(), name = 'admitpatient'),
    re_path('admissions/', AdmissionsView.as_view(), name = 'admissions'),
    re_path(r'^(?P<id>\d+)/$', AdmissiondetailView.as_view(), name='admissiondetail'), 
    # re_path('clinic/', ClinicView.as_view(), name='clinic'),
    # re_path('theatrepatients/', TheatreView.as_view(), name='theatrepatients'),
    # re_path('theatreanalysis/', views.theatreanalysis, name='theatreanalysis'),
    # re_path('sendsms/', SMSSenderView.as_view(), name='sendsms'),
    # #re_path('searchbooking/', ClinicAnalysisView.as_view(), name='searchbooking'),
    # re_path('searchbooking/', views.clinicanalysis, name='searchbooking' ),
    # re_path('saveoutreach/', ContactView.as_view(), name = 'saveoutreach'),
    # re_path('outreach/', OutreachView.as_view(), name='outreach'),
    # re_path('graphicalclinicanalysis/', views.graphicalclinicanalysis, name='graphicalclinicanalysis'),
    # re_path(r'^(?P<id>\d+)/$', BookclinicdetailView.as_view(), name='clinicdetail'),   
    # re_path(r'^(?P<id>\d+)/editfile/$', PostUpdateView.as_view(), name='editfile'),
]