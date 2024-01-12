# forms.py
from django import forms
from images.models import Newid
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms





#####try with new
class NewidForm(forms.ModelForm):
    class Meta:
        model = Newid
        fields = ('first_name','patientid',
         'id_number')   
