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
from .forms import NewUserForm ,ClinicSearchForm
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
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from taggit.models import Tag
from . import models, forms
from django.db.models import Avg, Count
#from .plotly_plot import *
#from .Dash_Apps import dash_plot
from Levenshtein import distance
#haystack
def error_404(request, exception):
        data = {}
        return render(request,'home/404.html', data)

def error_500(request,  exception):
        data = {}
        return render(request,'home/500.html', data)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="home/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="home/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home:login")



def analysis(request):
    sales_df = None
    chart = None
    no_data = None
    search_form = PatientSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')
        print(date_from, date_to, chart_type)
        sales_qs = Post.objects.filter(created_at__lte=date_to, created_at__date__gte=date_from)
    
        if len(sales_qs) > 0:
            sales_df = pandas.DataFrame(sales_qs.values())
            print(sales_df)

            sales_df['created_at'] = sales_df['created_at'].apply(lambda x: x.strftime('%d/%m/%Y'))
            sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1,
                            inplace=True)

            chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()

        else:
            messages.warning(request, "Apparently no data available...")

    context = {
        'search_form': search_form,
        'sales_df': sales_df,
        'chart': chart,
    }
    return render(request, 'home/analysis.html',  context)


@method_decorator(login_required, name='dispatch')
# class HomeView(ListView):
#     template_name = 'home/home.html'
#     model = Post
#     form_class = NewsletterForm
#     paginate_by = 1
#     queryset = Post.objects.all()

#     def spellcheck(self, query, threshold=3):
#         suggestions = []
#         for post in Post.objects.all():
#             for name in [post.first_name, post.second_name]:
#                 if distance(query.lower(), name.lower()) <= threshold:
#                     suggestions.append(name)
#         return list(set(suggestions))

#     def get(self, request):
#         context = {}
#         search_post = request.GET.get('search')
#         if search_post:
#             # check for misspellings
#             suggestions = self.spellcheck(search_post)
#             if suggestions:
#                 context['suggestions'] = suggestions
#                 return render(request, 'home/home.html', context)

#             # regular search
#             names = search_post.split()
#             q_objects = Q()
#             for name in names:
#                 q_objects |= Q(first_name__icontains=name) | Q(second_name__icontains=name)
#             posts = Post.objects.filter(q_objects).distinct()
#         else:
#             posts = Post.objects.all()

#         paginator = Paginator(posts, 100)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context['page_obj'] = page_obj
#         context['posts'] = posts

#         args = {
#             'posts': posts,
#             'page_number': page_number,
#             'page_obj': page_obj,
#         }
#         return render(request, self.template_name, args)
class HomeView(ListView):
    template_name = 'home/home.html'
    model = Post
    form_class = NewsletterForm
    paginate_by = 1
    queryset = Post.objects.all()


    def get(self, request):
        context = {}
        #form = NewsletterForm()
        #posts = Post.objects.all()
        #homepages = Homepage.objects.all() 
        search_post = request.GET.get('search')
        if search_post:
            posts = Post.objects.filter(Q(first_name__icontains=search_post) | Q(second_name__icontains=search_post)
             | Q(id_number__icontains=search_post) | Q(file_number__icontains=search_post)
             | Q(created_at__icontains=search_post)| Q(patient_category__icontains=search_post)| Q(phone_number__icontains=search_post))
        else:
            posts = Post.objects.all()
            print('file not found')
            #objects = objects.filter(field_one=search_post)



        #id_number = User.objects.get(id_number = Post.objects.get(id_number = request.Post.id_number))
        post = Post.objects.all()
        paginator = Paginator(posts,100)
        page = request.GET.get('page')
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['posts'] = posts


        args = {
            'posts': posts,  "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.user = request.user
            newsletter.save()
            title = 'Thanks!!'
            confirm_message = "Thankyou for subscribing to our newsletter, Email received"
            context = {'title': title, 'confirm_message': confirm_message }
            
        return render(request, self.template_name, context)

#def search(request):
#    product_list = Post.objects.all()
    #product_filter = PostFilter(request.GET, queryset=product_list)
#    return render(request, 'home/home.html', {'product_list': product_list})


@method_decorator(login_required, name='dispatch')
class AboutView(TemplateView):
    template_name = 'home/about.html'


    def get(self, request):
        posts = Post.objects.all()
        posts = Post.objects.all()
        paginator = Paginator(posts, 50)
        page = request.GET.get('page')
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        args = {
            'posts': posts, "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)

#this class view is for registering patients (latter with a unique code number)
@method_decorator(login_required, name='dispatch')
class ContactView(TemplateView):
    template_name = 'home/contact.html'
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
        form = PostForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Success!!'
            confirm_message = 'Patient Registered Successfully!'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)

from taggit.managers import TaggableManager
import qrcode
from io import BytesIO
import base64
import json

# class PostdetailView(TemplateView):
#     template_name = 'home/postdetail.html'
#     fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
#     model = Post

#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)

#         # Generate QR code image with post data
#         post_data = {
#             'id': post.id,
#             'title': post.id_number,
#             'body': post.file_number,
#             # Add any other fields you want to include in the QR code
#         }
#         url = reverse('home:postdetail', args=[str(post.id)])
#         url += f'?post_data={json.dumps(post_data)}'
#         qr = qrcode.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(request.build_absolute_uri(url))
#         qr.make(fit=True)
#         qr_img = qr.make_image(fill_color="black", back_color="white")

#         # Convert image to base64 format
#         buffer = BytesIO()
#         qr_img.save(buffer, format='PNG')
#         img_str = base64.b64encode(buffer.getvalue()).decode()

#         similar_posts = Post.objects.raw('SELECT * FROM post WHERE phone_number =%s',[id])

#         args = {'post': post, 'similar_posts': similar_posts, 'qr_code': img_str }

#         return render(request, self.template_name, args)


class PostdetailView(TemplateView):
    template_name = 'home/postdetail.html'
    fields = ['first_name', 'second_name', 'phone_number', 'file_number', 'id_number', 'patient_category']
    model = Post

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        associated_posts = post.associated_posts.all()

        # Generate QR code image
        url = reverse('home:postdetail', args=[str(post.id)])
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(request.build_absolute_uri(url))
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to base64 format
        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()

        args = {'post': post, 'associated_posts': associated_posts, 'qr_code': img_str}

        return render(request, self.template_name, args)

# class PostdetailView(TemplateView):
#     template_name = 'home/postdetail.html'
#     fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
#     model = Post

#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)

#         # Generate QR code image
#         url = reverse('home:postdetail', args=[str(post.id)])
#         qr = qrcode.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(request.build_absolute_uri(url))
#         qr.make(fit=True)
#         qr_img = qr.make_image(fill_color="black", back_color="white")

#         # Convert image to base64 format
#         buffer = BytesIO()
#         qr_img.save(buffer, format='PNG')
#         img_str = base64.b64encode(buffer.getvalue()).decode()

#         similar_posts = Post.objects.raw('SELECT * FROM post WHERE phone_number =%s',[id])

#         args = {'post': post, 'similar_posts': similar_posts, 'qr_code': img_str }

#         return render(request, self.template_name, args)
# class PostdetailView(TemplateView):
#     template_name = 'home/postdetail.html'
#     fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
#     model = Post

#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)

#         # Generate QR code image
#         url = reverse('home:postdetail', args=[str(post.id)])
#         qr = qrcode.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(request.build_absolute_uri(url))
#         qr.make(fit=True)
#         qr_img = qr.make_image(fill_color="black", back_color="white")

#         similar_posts = Post.objects.raw('SELECT * FROM post WHERE phone_number =%s',[id])

#         args = {'post': post, 'similar_posts': similar_posts, 'qr_code': qr_img }

#         return render(request, self.template_name, args)
# #this is the view that show more about the post(file details)
# class PostdetailView(TemplateView):
#     template_name = 'home/postdetail.html'
#     fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
#     model = Post

#     def get(self, request,id):
#         post = get_object_or_404(Post, id=id)
#         similar_posts = Post.objects.raw('SELECT * FROM post WHERE phone_number =%s',[id])
#         #similar_posts = Post.objects.filter(id_number=id_number)
            
#         #tags = TaggableManager() 
#         #similar_posts = get_object_or_404(Post,id=id)#filter( id_number__in=post_tags_ids)
#         #post_tag = Post.tags.all()
#         # List of similar posts
#             # List of similar posts
#         #post_tags_ids = post.tags.values_list('id_number', flat=True)
#         #similar_posts = Post.id_number.filter().exclude(id=post.id)
#         #similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
#         #similar_posts = post.object.tags.similar_object()
#         #return render(request, 'post_detail.html',{'post':post,'comments': comments,'comment_form':comment_form,'similar_posts':similar_posts})


#         args = {'post': post, 'similar_posts': similar_posts }
        
#         return render(request,self.template_name, args) 

#this class is for updating file details
#@method_decorator([login_required, staff_required], name='dispatch')


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

@superuser_required()
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
    template_name = 'home/editfile.html'

    success_url = reverse_lazy('tasks')

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = PostForm(request.POST or None, instance = post)
        

        args = {
            'form': form,'post': post
        }
        return render(request, self.template_name, args) 
    
    def post(self,request,id):
        post = get_object_or_404(Post, id=id)
        form = PostForm(request.POST or None, instance = post)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Success!!'
            confirm_message = 'Patient File Edited Successfully!'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)



#this class is for creating new files with a unique code number
@method_decorator(login_required, name='dispatch')
class CreateNewView(TemplateView):
    template_name = "home/createnewfile.html"
    model = New
    form_class = NewForm


    def get(self, request):
        form = NewForm()
        #file_no = request.

        args = {
            'form':form,# 'file_no':file_no
        }
        return render(request, self.template_name, args)

    def post(self,request):
        form = NewForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Success!!'
            confirm_message = 'New File Created Successfully'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)



@method_decorator(login_required, name='dispatch')
class NewFilesView(TemplateView):
    template_name = "home/newfiles.html"
    model = New
    form_class = NewForm

    def get(self, request):
        posts = New.objects.filter().order_by('-created_at')
        paginator = Paginator(posts, 50)
        page = request.GET.get('page')
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        args = {
            'posts': posts, "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)  


@method_decorator(login_required, name='dispatch')
class SortView(TemplateView):
    template_name = 'home/sorted.html'
    model = Post

    def get(self , request):
        posts = Post.objects.order_by('-id_number')
        
        paginator = Paginator(posts, 100)
        page = request.GET.get('page')
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        args = {'posts': posts, "page_number":page_number, "page_obj":page_obj, "page_number":page_number }

        return render(request, self.template_name, args)

@method_decorator(login_required, name='dispatch')
class ApointmentTemplateView(TemplateView):
    template_name = "home/appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Apointment.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            phone = mobile,
            request= message,
        )
        appointment.save()
        title = 'Success'
        confirm_message = 'Booking Requested Successfully!'
        context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context) 
        #appointment.save()

        #message.add_message(request, messages.SUCCESS, f"Thanks {fname} for making")
        #return HttpResponseRedirect(request.path)


@method_decorator(login_required, name='dispatch')
class ManageAppointmentTemplateView(ListView):
    template_name = "home/manage-apointments.html"
    model = Apointment
    context_object_name = "appointments"
    paginate_by = 9

    ##def get(self, request):
        #no_of_appointments = Apointment.objects.count()

        #args = {"no_of_appointments": no_of_appointments}

        #return render(request, self.template_name, args)
    

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        no_of_appointments = Apointment.objects.count()
        appointment = Apointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        appointment.save()
        title = 'Success'
        confirm_message = 'Patient Booked Successfully!'
        context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)


        #data = {
        #    "fname": appointment.first_name,
        #    "date": date,
        #    "no_of_appointments": no_of_appointments
        #}

        #message = get_template('home/manage-apointments.html').render(data)
        #email = EmailMessage(
        #    "About your appointment",
        #    message,
        #    settings.EMAIL_HOST_USER,
        #    [appointment.email],
        #)
        #email.content_subtype = "html"
        #email.send()

        #message.add_message(request, message.SUCCESS, f"You accepted tje appointment")
        #return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        appointments = Apointment.objects.all()
        context.update({
            "title":"Manage Appointments"
        })
        return context


@method_decorator(login_required, name='dispatch')
class HospitalAppointmentsView(ListView):
    template_name = "home/hospitalappointments.html"
    model = Apointment
    context_object_name = "appointments"
    paginate_by = 50


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        no_of_appointments = Apointment.objects.all()
        appointment = Apointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,
            "no_of_appointments": no_of_appointments
        }

        message = get_template('home/email.html').render(data)
        #email = EmailMessage(
        #    "About your appointment",
        #    message,
        #    settings.EMAIL_HOST_USER,
        #    [appointment.email],
        #)
        #email.content_subtype = "html"
        #email.send()

        messages.add_message(request, constants.SUCCESS, f"You accepted tje appointment")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        appointments = Apointment.objects.all()
        context.update({
            "title":"Manage Appointments"
        })
        return context


def clinicanalysis(request):
    
    #0no_data = None
    search_form = ClinicSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        
        results_by = request.POST.get('results_by')
        print(date_from, date_to)
        sales_qs = Post.objects.filter(created_at__lte=date_to, created_at__gte=date_from)
        

    context = {
        'search_form': search_form,
       
    }
    return render(request, 'home/searchappointments.html',  context)
