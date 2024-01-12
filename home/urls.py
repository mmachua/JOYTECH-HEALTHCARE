from django.conf.urls import url
from django.urls import include, re_path, path
from home.views import HomeView, AboutView, ContactView, PostdetailView,SortView,PostUpdateView, ApointmentTemplateView, ManageAppointmentTemplateView#, HospitalAppointments
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from home import views 
from . import views 
from home.views import HospitalAppointmentsView, CreateNewView, NewFilesView#,# index # MySearchView
#from .views import update
from .views import  register_request, login_request, logout_request, analysis,clinicanalysis, error_404
#from . import search_indexes # or import simpleexample
app_name = 'home'

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    #path('index', views.index, name='index'),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^analysis/$', views.analysis, name="analysis"),
    re_path(r'^clinicanalysis/$', views.clinicanalysis, name="clinicanalysis"),
    re_path(r'^(?P<id>\d+)/$', PostdetailView.as_view(), name='postdetail'),
    re_path(r'^(?P<id>\d+)/editfile/$', PostUpdateView.as_view(), name='editfile'),
    #path('update/<str:id>/', update, name="update"),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^contact/$', ContactView.as_view(), name='contact'),
    re_path(r'newfiles/$', NewFilesView.as_view(), name='newfiles'),
    re_path(r'^createnewfile/$', CreateNewView.as_view(), name='createnewfile'),
    #re_path(r'^search/$', views.search, name='search'),
    #path('search/', SearchView.as_view(), name='search'),
    re_path(r'^sorted/$', SortView.as_view(), name='sorted'),
    path("make-an-appointment/", ApointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("hospitalappointments/", HospitalAppointmentsView.as_view(),name='hospitalappointment'),
    path("logout", views.logout_request, name= "logout"),
]

handler404 = 'home.views.error_404'
