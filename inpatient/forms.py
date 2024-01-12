from django import forms
from inpatient.models import Admission, PatientNote # Newsletter
#from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import FormView

#from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
#from .widgets import BootstrapDateTimePickerInput

class AdmitForm(forms.ModelForm):
    dateofadmission = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Admission
        fields = ('firstname','lastname','phone','ward','bedno','fileno','dateofadmission')
       


    def save(self, user=None):
        post = super(AdmitForm, self).save(commit=True)
        #if User:
        #    post.User = user
        post.save()
        return post

class PatientNoteForm(forms.ModelForm):
    note = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = PatientNote
        fields = ['note']

class AddNoteView(FormView):
    template_name = 'inpatient/add_note.html'
    form_class = PatientNoteForm

    def form_valid(self, form):
        patient = get_object_or_404(Admission, id=self.kwargs['pk'])
        note = form.save(commit=False)
        note.patient = patient
        note.doctor = self.request.user
        note.save()
        return redirect('admission_detail', id=patient.id)
