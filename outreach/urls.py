from django.conf.urls import url
from django.urls import include, re_path, path
from outreach.views import ContactView, OutreachView, BookclinicView, ClinicView,graphicalclinicanalysis,clinicanalysis, BooktheatreView
from outreach.views import  BookclinicdetailView, PostUpdateView, SMSSenderView, TheatreView, theatreanalysis, WhatsAppSenderView
from . import views 


app_name = 'outreach'

urlpatterns = [
    re_path('bookclinic/', BookclinicView.as_view(), name = 'bookclinic'),
    re_path('booktheatre/', BooktheatreView.as_view(), name = 'booktheatre'),
    re_path('clinic/', ClinicView.as_view(), name='clinic'),
    re_path('theatrepatients/', TheatreView.as_view(), name='theatrepatients'),
    re_path('theatreanalysis/', views.theatreanalysis, name='theatreanalysis'),
    re_path('sendsms/', SMSSenderView.as_view(), name='sendsms'),
    re_path('sendwhatsappmessage/', WhatsAppSenderView.as_view(), name='sendwhatsappmessage'),
    #re_path('searchbooking/', ClinicAnalysisView.as_view(), name='searchbooking'),
    re_path('searchbooking/', views.clinicanalysis, name='searchbooking' ),
    re_path('saveoutreach/', ContactView.as_view(), name = 'saveoutreach'),
    re_path('outreach/', OutreachView.as_view(), name='outreach'),
    re_path('graphicalclinicanalysis/', views.graphicalclinicanalysis, name='graphicalclinicanalysis'),
    re_path(r'^(?P<id>\d+)/$', BookclinicdetailView.as_view(), name='clinicdetail'),   
    re_path(r'^(?P<id>\d+)/editfile/$', PostUpdateView.as_view(), name='editfile'),
    re_path('tetris/', views.tetris_view, name='tetris'),
]

#handler404 = 'home.views.error_404'
