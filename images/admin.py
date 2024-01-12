from django.contrib import admin
from .models import  Newid


admin.site.register(Newid)

# class PatientIdUploadAdmin(admin.ModelAdmin):
#     list_display = ['idno','patientid']
# admin.site.register(PatientIdUpload, PatientIdUploadAdmin)

