from datetime import datetime
from turtle import title
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Post, Homepage, Aboutpage
from django.views.generic import ListView, CreateView 
from home.forms import ContactForm, NewsletterForm, PostForm, NewForm, PatientSearchForm
from home.models import Contact, Newsletter, Apointment,New
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime
from django.template.loader import get_template
#from haystack.generic_views import SearchView
#from django.contrib.postgres.operations import UnaccentExtension, TrigramExtension 
#from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
from datetime import date
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import  render, redirect
#from qrcode import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import pandas
from home.utils import get_chart
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connections
from django.contrib import messages
from django.urls import reverse
import pandas as pd
#import pymysql.cursors
from plotly.offline import plot
import plotly.graph_objs as go


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  NewidForm
from .models import Newid








class DisplayhotelimagesView(ListView):
	template_name = 'imagesuploaded.html'
	model = Newid
	form_class = Newid
	paginate_by = 1
	queryset = Newid.objects.all()


	def get(self, request):
		hotels = Newid.objects.all().order_by('-id')
		context = {}
		search_hotel = request.GET.get('search')
		if search_hotel:
			hotels = Newid.objects.filter(
              Q(id_number__icontains=search_hotel)|
			  Q(first_name__icontains=search_hotel)
             )
		else:
			hotels = Newid.objects.all()

			
		hotel = Newid.objects.all().order_by('-id')
		paginator = Paginator(hotels,100)
		page = request.GET.get('page')
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context['page_obj'] = page_obj
		context['hotels'] = hotels

		args = {
			'hotel_images': hotels, 'hotels':hotels,   "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
		}
		return render(request, self.template_name, args)


#######try with newfiles
class CreateNewidView(TemplateView):
    template_name = 'images.html'
    model = Newid
    form_class = NewidForm


    def get(self, request):
        form = NewidForm()
        #file_no = request.

        args = {
            'form':form,# 'file_no':file_no
        }
        return render(request, self.template_name, args)

    def post(self,request):
        form = NewidForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Success!!'
            confirm_message = 'Successfully Sent Document'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)


def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['contact']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save()
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')