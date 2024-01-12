from django.db import models
from django.db import models
from django.contrib.auth.models import User
#from utils import create_new_ref_number
from uuid import uuid4
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.\


#save admission
class Admission(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    #secondname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    ward = models.CharField(max_length=30, blank=False,choices=(
                                            ('FEMALE_MEDICAL_WARD','FEMALE MEDICAL WARD'),
                                            ('MALE_MEDICAL_WARD','MALE MEDICAL WARD'),
                                            ('SURGICAL_WARD','SURGICAL WARD'),
                                            ('MALE_SURGICAL_WARD','MALE SURGICAL WARD'),
                                            ('FEMALE_SURGICAL_WARD','FEMALE SURGICAL WARD'),
                                            ('MARTERNITY_WARD','MARTERNITY WARD'),
                                            ('FEMALE_MEDICAL_WARD','FEMALE MEDICAL WARD'),
                                            ('GEATRIC_WARD','GEATRIC WARD'),
                                            ('PAEDIATRICS','PAEDIATRICS')                                 

                                            ))
    bedno = models.CharField(max_length=30, blank=False)
    fileno = models.CharField(max_length=30, blank=False)
    dateofadmission = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ('-dateofadmission', )

    def get_absolute_re_path(self):
        return reverse('inpatient:admissiondetail',args=[self.id])


class PatientNote(models.Model):
    patient = models.ForeignKey(Admission, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"Note for {self.patient.firstname} by {self.doctor.username}"
