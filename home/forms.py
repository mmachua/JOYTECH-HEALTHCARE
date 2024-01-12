from django import forms
from home.models import Contact, Newsletter, Post, Homepage, Aboutpage, New
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

CHART_CHOICES = (
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)
RESULTS_CHOICES = (
    ('#1', 'Age'),
    ('#2', 'patient_category'),
    #('#3', 'Customer ID'),
    #('#4', 'Total Price')
)

class ClinicSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    


class PatientSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    results_by = forms.ChoiceField(choices=RESULTS_CHOICES)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('first_name', 'second_name', 'phone_number',
        'file_number', 'age', 'id_number', 'patient_category')


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('first_name', 'second_name', 'phone_number',
         'age', 'id_number', 'patient_category','file_no')   


class ContactForm(forms.ModelForm):
    phone  = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your phone number here...'
        }
    ))
    class Meta:
        model = Contact

        fields = [
            'name',
            'email',
            'content'
            
        ]

class NewsletterForm(forms.ModelForm):

    attrs={
        'class':'form-control',
        'placeholder': 'Write your email here...'
    }
    class Meta:
        model = Newsletter
        fields = [
            'email'
       ]