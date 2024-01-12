from django.contrib import admin

# Register your models here.
from .models import Admission, PatientNote

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','phone','ward','dateofadmission']
admin.site.register(Admission, AdmissionAdmin)
# Register your models here.
class PatientNoteAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','note','created_at']
admin.site.register(PatientNote, PatientNoteAdmin)