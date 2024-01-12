"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.conf.urls import url, include, re_path
from django.urls import path
from django.conf import settings
#from login.views import  client, shop, login
from django.conf.urls.static import static
from home.views import error_404
import django.views.defaults

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    re_path(r'records/', include('records.urls',namespace='records')),
    re_path(r'inpatient/', include('inpatient.urls',namespace='inpatient')),
    re_path(r'outreach/',  include('outreach.urls',namespace='outreach')),
    re_path(r'inventory/',  include('inventory.urls',namespace='inventory')),

    re_path(r'images/', include('images.urls',namespace='images')),
    url(r'^404/$', django.views.defaults.page_not_found, ),
    path("500/", custom_server_error),
    #path('search/', include('haystack.urls')),
    #path('django_plotly_dash/', include('django_plotly_dash.urls')),

]
handler404 = 'home.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)