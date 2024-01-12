from django.shortcuts import render
from .models import Admission, PatientNote
# Create your views here.
from django.shortcuts import render
from re import search
from django.shortcuts import render

from datetime import datetime
from turtle import title
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from django.views.generic import ListView, CreateView,UpdateView 
#from home.forms import ContactForm, NewsletterForm, PostForm, NewForm, PatientSearchForm
from home.models import Contact, Newsletter, Apointment,New
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime
from django.template.loader import get_template
from outreach.forms import PostForm, BookclinicForm, FilterclinicForm, GraphclinicForm, BooktheatreForm, FiltertheatreForm
from inpatient.forms import AdmitForm
from outreach.models import Post, Booktheatre, Bookclinic
from home.forms import NewUserForm , PatientSearchForm,ClinicSearchForm
# Create your views here.
from django.contrib import messages
import pandas
import pandas as pd

from dateutil.parser import parse
from datetime import timedelta
from datetime import datetime
from pandas.tseries.offsets import Hour, Minute
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from outreach import send_sms
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from twilio.rest import Client
#book clinic
#  
class AdmitView(TemplateView):
    template_name = 'inpatient/admit.html'
    model = Admission
    form_class = AdmitForm

    def get(self, request):
        form = AdmitForm()

        args = {
            'form': form
        }
        return render(request, self.template_name, args)

        #return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = AdmitForm(request.POST,request.FILES)


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
            confirm_message = 'Error not Registered!'
            title = 'Not Saved!!'
            args = {'title': title, 'confirm_message': confirm_message }
            title = 'Success!!'
            confirm_message = 'Clinic Edited Successfully!'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name)#, context)


#View Clinic Booked Patients
class AdmissionsView(ListView):
	template_name = 'inpatient/admitted.html'
	model = Admission
	#form_class = PostForm
	paginate_by = 1
	queryset = Post.objects.all()


	def get(self, request):
		
		context = {}
		search_post = request.GET.get('search')
		if search_post:
			posts = Admission.objects.filter(
              Q(firstname__icontains=search_post) |Q(ward__icontains=search_post)|Q(lastname__icontains=search_post)|Q(fileno__icontains=search_post)| Q(phone__icontains=search_post)
             )
		else:
			posts = Admission.objects.all()

			
		post = Admission.objects.all().order_by('dateofadmission')
		paginator = Paginator(posts,100)
		page = request.GET.get('page')
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context['page_obj'] = page_obj
		context['posts'] = posts

		args = {
			'posts': posts, 'post':post, "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
		}

		return render(request, self.template_name, args)

class AdmissiondetailView(TemplateView):
    template_name = 'inpatient/admissiondetail.html'

    def get(self, request, id):
        post = get_object_or_404(Admission, id=id)
        notes = PatientNote.objects.filter(patient=post)
        args = {'post': post, 'notes': notes}
        return render(request, self.template_name, args)

# class AdmissiondetailView(TemplateView):
#     template_name = 'inpatient/admissiondetail.html'
#     fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
#     model = Admission

#     def get(self, request,id):
#         post = get_object_or_404(Admission, id=id) 
#         args = {'post': post }
#         return render(request,self.template_name, args) 

