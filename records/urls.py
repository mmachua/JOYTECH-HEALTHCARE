import imp
from django.conf.urls import url
from django.urls import include, re_path
#from homee.views import HomeView, CreateView,AboutView, Post_detailView, PostFormView 
from django.contrib.auth import views as auth_views
from . import views as myapp_views
#from records.forms import HomeForm
#from homee import views
from . import views 
from records.views import ContactView, DisplaydocumentsView

app_name = 'records'
urlpatterns = [
    #re_path(r'^$', HomeView.as_view(), name='home'),
    
    re_path(r'^display/$', DisplaydocumentsView.as_view(), name='display'),
 
    re_path('post/', ContactView.as_view(), name = 'post'),

    #re_path(r'^(?P<id>\d+)/$', Post_detailView.as_view(), name='post_detail'),
    
   
]