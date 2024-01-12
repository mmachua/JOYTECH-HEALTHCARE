from django import forms
from outreach.models import Post ,Bookclinic, Booktheatre # Newsletter
#from django.contrib.auth.models import User
from django.conf import settings
#from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .widgets import BootstrapDateTimePickerInput


class PostForm(forms.ModelForm):
    # post = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Write the Name of the Document...'
    #     }
    # ))
    # document = forms.FileField()

    class Meta:
        model = Post
        fields = ('firstname','lastname','idno','phone','oureachlocation','dx','followup')
        
    def save(self, user=None):
        post = super(PostForm, self).save(commit=True)
        #if User:
        #    post.User = user
        post.save()
        return post


class BookclinicForm(forms.ModelForm):
    tcadate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Bookclinic
        fields = ('firstname','lastname','phone','tcadate','clinic','doctornote')
       


    def save(self, user=None):
        post = super(BookclinicForm, self).save(commit=True)
        #if User:
        #    post.User = user
        post.save()
        return post

class BooktheatreForm(forms.ModelForm):
    dateofoperation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booktheatre
        fields = ('firstname','lastname','phone','dateofoperation','typeofoperation','doctor')
       


    def save(self, user=None):
        post = super(BooktheatreForm, self).save(commit=True)
        #if User:
        #    post.User = user
        post.save()
        return post


class FiltertheatreForm(forms.Form):  
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #chart_type = forms.ChoiceField(choices=CHART_CHOICES)



CHART_CHOICES = (
    ('#1', 'ALL'),
    ('#2', 'POPC'),
    ('#3', 'MOPC'),
    ('#4', 'ENT'),
    ('#5', 'ENDOSCOPY'),
    ('#6', 'ORTHOPAEDIC'),
    ('#7', 'ONCOLOGY'),
    ('#8', 'OPTHAMOLOGY'),
    ('#9', 'DENTAL'),
    ('#10', 'SOPC'),
    ('#2', 'GOPC'),
)


# RESULTS_CHOICES = (
#     ('#1', 'Age'),
#     ('#2', 'patient_category'),
#     #('#3', 'Customer ID'),
#     #('#4', 'Total Price')
# )



class FilterclinicForm(forms.Form):  
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #chart_type = forms.ChoiceField(choices=CHART_CHOICES)


CHART_CHOICESS =(
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)

RESULTS_CHOICESS = (
    ('#1', 'tcadate'),
    ('#2', 'tcadate'),
    #('#3', 'Customer ID'),
    #('#4', 'Total Price')
)


class GraphclinicForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICESS)
    #results_by = forms.ChoiceField(choices=RESULTS_CHOICESS)