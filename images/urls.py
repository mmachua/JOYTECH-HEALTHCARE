from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from images.views import DisplayhotelimagesView , CreateNewidView #,hotel_image_view #, display_hotel_images
from images import views
app_name = 'images'
urlpatterns = [
	#re_path(r'^images/$', HotelImageView.as_view(), name='images'),
	re_path(r'images/$', CreateNewidView.as_view(), name='images'),
	
	re_path(r'^imagesuploaded/$', DisplayhotelimagesView.as_view(), name='imagesuploaded'),
	#path('images/', views.hotel_image_view, name = 'images'),
	# path('success', success, name = 'success'),
	#path('imagesuploaded/', views.display_hotel_images, name = 'imagesuploaded'),
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)
