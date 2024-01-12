from re import search
from django.shortcuts import render

from datetime import datetime
from turtle import title
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from django.views.generic import ListView, CreateView 
#from home.forms import ContactForm, NewsletterForm, PostForm, NewForm, PatientSearchForm
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


 #  NewUserForm ,ClinicSearchForm

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
from records.models import Post
from records.forms import PostForm
#from .plotly_plot import *
#from .Dash_Apps import dash_plot

#h


# Create your views here.
class ContactView(TemplateView):
    template_name = 'contact.html'
    model = Post
    form_class = PostForm

    def get(self, request):
        form = PostForm()

        args = {
            'form': form,# "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)

        #return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = PostForm(request.POST,request.FILES)


        if form.is_valid():
            post = form.save()#commit=False)
            post.user = request.user
            post.save()
            #post.user = request.user
            ##print("contact")
            post.save()
            title = 'Success!!'
            confirm_message = 'Patient Registered Successfully!'
        else:
            confirm_message = 'Error Id not Registered!'
            title = 'Not Saved!!'
            context = {'title': title, 'confirm_message': confirm_message }
            
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name)#, context)


class DisplaydocumentsView(ListView):
	template_name = 'documents.html'
	model = Post
	form_class = PostForm
	paginate_by = 1
	queryset = Post.objects.all()


	def get(self, request):
		#Hotels = PatientIdUpload.objects.all()#.order_by('-id')
		context = {}
		search_post = request.GET.get('search')
		if search_post:
			posts = Post.objects.filter(
              Q(post__icontains=search_post)
             )
		else:
			posts = Post.objects.all()

			
		post = Post.objects.all().order_by('-id')
		paginator = Paginator(posts,100)
		page = request.GET.get('page')
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context['page_obj'] = page_obj
		context['posts'] = posts

		args = {
			'posts': posts, "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
		}
		return render(request, self.template_name, args)
