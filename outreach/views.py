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
from outreach.models import Post, Booktheatre, Bookclinic
from home.forms import NewUserForm , PatientSearchForm,ClinicSearchForm
# Create your views here.
from django.contrib import messages
import pandas
import pandas as pd
from .utils import get_chart
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
#from send_sms import send_sms
#Send SMS
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from twilio.rest import Client
from django.contrib import messages
from django.urls import reverse


def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

#save outreach
class ContactView(TemplateView):
    template_name = 'outreach/saveoutreach.html'
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



#View Outreach
class OutreachView(ListView):
	template_name = 'outreach/outreach.html'
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



#book clinic 
class BookclinicView(TemplateView):
    template_name = 'outreach/bookclinic.html'
    model = Bookclinic
    form_class = BookclinicForm

    def get(self, request):
        form = BookclinicForm()

        args = {
            'form': form,# "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)

        #return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = BookclinicForm(request.POST,request.FILES)


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

#book Theatre
class BooktheatreView(TemplateView):
    template_name = 'outreach/booktheatre.html'
    model = Booktheatre
    form_class = BooktheatreForm

    def get(self, request):
        form = BooktheatreForm()

        args = {
            'form': form,# "page_number":page_number, "page_obj":page_obj, "page_number":page_number,
        }
        return render(request, self.template_name, args)

        #return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = BooktheatreForm(request.POST,request.FILES)

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



#this is the view that show more about the post(file details)
class BookclinicdetailView(TemplateView):
    template_name = 'outreach/clinicdetail.html'
    fields = ['first_name','second_name','phone_number','file_number','id_number','patient_category']
    model = Bookclinic

    def get(self, request,id):
        post = get_object_or_404(Bookclinic, id=id) 
        args = {'post': post }
        return render(request,self.template_name, args) 


#View Clinic Booked Patients
class ClinicView(ListView):
	template_name = 'outreach/bookedclinics.html'
	model = Bookclinic
	#form_class = PostForm
	paginate_by = 1
	queryset = Post.objects.all()


	def get(self, request):
		
		context = {}
		search_post = request.GET.get('search')
		if search_post:
			posts = Bookclinic.objects.filter(
              Q(firstname__icontains=search_post) |Q(clinic__icontains=search_post)|Q(lastname__icontains=search_post)| Q(phone__icontains=search_post)
             )
		else:
			posts = Bookclinic.objects.all()

			
		post = Bookclinic.objects.all().order_by('tcadate')
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


#View Clinic Booked Patients
class TheatreView(ListView):
	template_name = 'outreach/bookedtheatrepatients.html'
	model = Booktheatre
	#form_class = PostForm
	paginate_by = 1
	queryset = Post.objects.all()


	def get(self, request):
		
		context = {}
		search_post = request.GET.get('search')
		if search_post:
			posts = Booktheatre.objects.filter(
              Q(firstname__icontains=search_post) |Q(clinic__icontains=search_post)|Q(lastname__icontains=search_post)| Q(phone__icontains=search_post)
             )
		else:
			posts = Booktheatre.objects.all()

			
		post = Booktheatre.objects.all().order_by('dateofoperation')
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

##Update Clinic Posts
@superuser_required()
class PostUpdateView(UpdateView):
    template_name='outreach/editbookedclinic.html'
    model = Bookclinic
    form_class = BookclinicForm
    fields = ['firstname','secondname','phone']
    

    #success_url = reverse_lazy('tasks')

    def get(self, request, id):
        post = get_object_or_404(Bookclinic, id=id)
        form = BookclinicForm(request.POST or None, instance = post)
        

        args = {
            'form': form,'post': post
        }
        return render(request, self.template_name, args) 
    
    def post(self,request,id):
        post = get_object_or_404(Bookclinic, id=id)
        form = BookclinicForm(request.POST or None, instance = post)
        if form.is_valid():
            contact = form.save()
            contact.user = request.user
            contact.save()
            title = 'Success!!'
            confirm_message = 'Clinic Edited Successfully!'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)

#Analyze Theatre Clinics
def theatreanalysis(request):
    sales_df = None
    chart = None
    no_data = None
    search_form = FiltertheatreForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        # = request.POST.get('chart_type')
        #results_by = request.POST.get('results_by')
        print(date_from, date_to)#, chart_type)
        sales_qs = Booktheatre.objects.filter(dateofoperation__lte=date_to, dateofoperation__gte=date_from)

        if len(sales_qs) > 0:
            sales_df = pandas.DataFrame(sales_qs.values())
            print(sales_df)

            sales_df['dateofoperation'] = sales_df['dateofoperation'].apply(lambda x: x.strftime('%d/%m/%Y'))
            sales_df.rename({'firstname': 'First Name', 'lastname': 'Last Name','dateofoperation': 'Date of Operation','phone': 'Phone Number','doctor': "Operating Doctor", 'typeofoperation': 'Type Of Operation'}, axis=1,
                            inplace=True)
            sales_df = sales_df.drop("date", axis='columns')
            sales_df = sales_df.drop("id", axis='columns')

            #chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()
        else:
            messages.warning(request, "Apparently no booked clinics on that period...")
    # if search_post:
    #     posts = Bookclinic.objects.filter(Q(firstname__icontains=search_post) | Q(secondname__icontains=search_post)
    #          | Q(phone__icontains=search_post))
    # else:
    #     posts = Post.objects.all()
    #     print('file not found')
    #     #objects = objects.filter(field_one=search_post)
    context = {
        'search_form': search_form,
        'sales_df': sales_df,
        #'posts': posts,
 
    }
    return render(request, 'outreach/searchtheatrebooking.html',  context)




#Analyze Clinics
def clinicanalysis(request):
    sales_df = None
    chart = None
    no_data = None
    search_form = FilterclinicForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')
        print(date_from, date_to, chart_type)
        sales_qs = Bookclinic.objects.filter(tcadate__lte=date_to, tcadate__gte=date_from)

        if len(sales_qs) > 0:
            sales_df = pandas.DataFrame(sales_qs.values())
            print(sales_df)

            sales_df['tcadate'] = sales_df['tcadate'].apply(lambda x: x.strftime('%d/%m/%Y'))
            sales_df.rename({'firstname': 'First Name', 'lastname': 'Last Name','tcadate': 'TCA Date','phone': 'Phone Number','doctornote': "Doctor's note", 'clinic': 'Clinic'}, axis=1,
                            inplace=True)
            sales_df = sales_df.drop("date", axis='columns')
            sales_df = sales_df.drop("id", axis='columns')

            #chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()
        else:
            messages.warning(request, "Apparently no booked clinics on that period...")
    # if search_post:
    #     posts = Bookclinic.objects.filter(Q(firstname__icontains=search_post) | Q(secondname__icontains=search_post)
    #          | Q(phone__icontains=search_post))
    # else:
    #     posts = Post.objects.all()
    #     print('file not found')
    #     #objects = objects.filter(field_one=search_post)



    context = {
        'search_form': search_form,
        'sales_df': sales_df,
        #'posts': posts,
 
    }
    return render(request, 'outreach/searchbooking.html',  context)


#Show Graphical interface of the clinics
def graphicalclinicanalysis(request):
    sales_df = None
    sales_df_all = None
    chart = None
    search_form = GraphclinicForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')

        sales_qs = Bookclinic.objects.filter(tcadate__lte=date_to, tcadate__gte=date_from)

        if len(sales_qs) > 0:
            sales_df_all = pd.DataFrame.from_records(Bookclinic.objects.all().values())
            sales_df_all['tcadate'] = pd.to_datetime(sales_df_all['tcadate']).dt.strftime('%d/%m/%Y')
            sales_df_all.rename(columns={'firstname': 'First Name', 'lastname': 'Last Name', 'tcadate': 'TCA Date',
                                         'phone': 'Phone Number', 'doctornote': "Doctor's note", 'clinic': 'Clinic'},
                                inplace=True)
            sales_df_all.drop(columns=['date', 'id'], inplace=True)
            sales_df_all.groupby('Clinic').describe()
            sales_df_all = sales_df_all.to_html()

            sales_df = pd.DataFrame.from_records(sales_qs.values())
            sales_df['tcadate'] = pd.to_datetime(sales_df['tcadate']).dt.strftime('%d/%m/%Y')
            sales_df.rename(columns={'firstname': 'First Name', 'lastname': 'Last Name', 'tcadate': 'TCA Date',
                                     'phone': 'Phone Number', 'doctornote': "Doctor's note", 'clinic': 'Clinic'},
                            inplace=True)
            sales_df.drop(columns=['date', 'id'], inplace=True)
            sales_df.groupby('Clinic').describe()
            chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()

        else:
            messages.warning(request, "Apparently no data available...")
            no_data = True

    total_clinics = Bookclinic.objects.values('clinic').distinct().count()

    context = {
        'search_form': search_form,
        'sales_df_all': sales_df_all,
        'sales_df': sales_df,
        'chart': chart,
        'total_clinics': total_clinics
    }
    return render(request, 'outreach/clinicanalysis.html', context)


import phonenumbers
from phonenumbers import NumberParseException




### this class helps send sms in bulk 
class SMSSenderView(TemplateView):
    template_name = 'outreach/send_sms.html'
    client = Client("AC742a2f89ccd", "2ff6742d9faf472ab16")

    def get(self, request):
        posts = Post.objects.all()
        args = {
            'posts': posts
        }
        return render(request, self.template_name, args)

    def post(self, request):
        message = request.POST.get('message')
        phone_numbers = request.POST.get('phone_numbers')

        # Lists to store successfully sent and failed phone numbers
        sent_numbers = []
        failed_numbers = []

        if phone_numbers:
            phone_numbers_list = phone_numbers.split(',')

            for phone_number in phone_numbers_list:
                # Normalize the phone number using the phonenumbers library
                try:
                    parsed_number = phonenumbers.parse(phone_number, "KE")
                    if not phonenumbers.is_valid_number(parsed_number):
                        raise NumberParseException(NumberParseException.INVALID_COUNTRY_CODE, "Invalid phone number")
                    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                except NumberParseException:
                    failed_numbers.append(phone_number.strip())
                    continue

                # Send SMS message to each normalized phone number
                try:
                    self.client.messages.create(
                        to=formatted_number,
                        from_="",
                        body=f"Hello,\n{message}\nMartin\nHRIO\n y Hospital" #replace y with the name of your hospital/org
                    )
                    sent_numbers.append(formatted_number)
                except Exception:
                    failed_numbers.append(phone_number.strip())

        # Display a confirmation message
        title = 'Thanks!!'
        confirm_message = "SMS sent successfully!"
        context = {
            'title': title,
            'confirm_message': confirm_message,
            'sent_numbers': sent_numbers,
            'failed_numbers': failed_numbers,
        }

        return render(request, self.template_name, context)

# class SMSSenderView(TemplateView):
#     template_name = 'outreach/send_sms.html'
#     client = Client("AC749a0e2abbc49ba53ac3ba52a2f89ccd", "2ff6742d9faf404bd5ed72904772ab16")

#     def get(self, request):
#         posts = Post.objects.all()
#         args = {
#             'posts': posts
#         }
#         return render(request, self.template_name, args)

#     def post(self, request):
#         message = request.POST.get('message')
#         phone_numbers = request.POST.get('phone_numbers')

#         if phone_numbers:
#             phone_numbers_list = phone_numbers.split(',')

#             # Send SMS message to each phone number
#             for phone_number in phone_numbers_list:
#                 self.client.messages.create(
#                     to=phone_number.strip(),  # Remove leading/trailing spaces
#                     from_="+16187063542",
#                     body=f"Hello,\n{message}\nMartin\nHRIO\nOljabet Hospital"
#                 )

#         # Display a confirmation message
#         title = 'Thanks!!'
#         confirm_message = "SMS sent successfully!"
#         context = {'title': title, 'confirm_message': confirm_message}

#         return render(request, self.template_name, context)

class WhatsAppSenderView(TemplateView):
    template_name = 'outreach/sendwhatsapp.html'
    client = Client("AC749a0e29ccd", "2ff6742d9faf72ab16")

    def post(self, request):
        message = request.POST.get('message')
        phone_numbers = request.POST.get('phone_numbers')

        # Lists to store successfully sent and failed phone numbers
        sent_numbers = []
        failed_numbers = []

        if phone_numbers:
            phone_numbers_list = phone_numbers.split(',')

            for phone_number in phone_numbers_list:
                # Normalize the phone number using the phonenumbers library
                try:
                    parsed_number = phonenumbers.parse(phone_number, "KE")
                    if not phonenumbers.is_valid_number(parsed_number):
                        raise NumberParseException(NumberParseException.INVALID_COUNTRY_CODE, "Invalid phone number")
                    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                except NumberParseException:
                    failed_numbers.append(phone_number.strip())
                    continue

                # Send WhatsApp message to each normalized phone number
                try:
                    self.client.messages.create(
                        to=f"whatsapp:{formatted_number}",
                        from_="whatsapp:+14155238886",
                        body=f"Hello,\n{message}\nMartin\nHRIO\n y Hospital"
                    )
                    sent_numbers.append(formatted_number)
                except Exception:
                    failed_numbers.append(phone_number.strip())

        # Display a confirmation message
        title = 'Whatsapp Message!!'
        confirm_message = "WhatsApp messages sent successfully!"
        context = {
            'title': title,
            'confirm_message': confirm_message,
            'sent_numbers': sent_numbers,
            'failed_numbers': failed_numbers,
        }

        return render(request, self.template_name, context)


def tetris_view(request):
    return render(request, 'outreach/tetris.html')