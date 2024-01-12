from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.conf import settings
#from django.contrib.auth import timezone


#save outreach patient
class Post(models.Model):
    firstname = models.CharField(max_length=500 ,blank=False)
    lastname = models.CharField(max_length=500 ,blank=False)
    idno = models.CharField(max_length=500 ,blank=False)
    phone = models.CharField(max_length=500 ,blank=False)
    oureachlocation = models.CharField(max_length=500 ,blank=False)
    dx = models.CharField(max_length=500 ,blank=False)
    followup = models.CharField(max_length=500 ,blank=False,choices=(
                                            ('Yes','Yes'),
                                            ('No','No')))
    
    date = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.firstname
    
        
    class Meta:
        ordering = ('-date', )



#book clinic model
class Bookclinic(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    tcadate = models.DateField(null=True, blank=True)
   
    clinic = models.CharField(max_length=30, blank=False,choices=(
                                            ('GOPC','GOPC'),
                                            ('POPC','POPC'),
                                            ('SOPC','SOPC'),
                                            ('MOPC','MOPC'),
                                            ('ENT','ENT'),
                                            ('ORTHOPAEDIC','ORTHOPAEDIC'),
                                            ('ONCOLOGY','ONCOLOGY'),
                                            ('OPTICAL','OPTICAL'),
                                            ('COLONOSCOPY','COLONOSCOPY'),
                                            ('ENDOCOPY','ENDOSCOPY'),
                                            ('DENTAL','DENTAL')

                                            ))
    doctornote = models.TextField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ('-tcadate', )

    def get_absolute_re_path(self):
        return reverse('outreach:clinicdetail',args=[self.id])



#book theatre patient
class Booktheatre(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    dateofoperation = models.DateField(null=True, blank=True)
   
    typeofoperation = models.CharField(max_length=30, blank=False,choices=(
                                            ('Caesarean_Section','Caesarean_Section'),
                                            ('General_Surgery','General_Surgery'),
                                            ('Thoracic_Surgery','Thoracic_Surgery'),
                                            ('Colon_and_Rectal_Surgery','Colon_and_Rectal_Surgery'),
                                           
                                            ('DENTAL','DENTAL')

                                            ))
    #doctornote = models.TextField(max_length=100, blank=False)
    doctor = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    class Meta:
        ordering = ('-dateofoperation', )

    def get_absolute_re_path(self):
        return reverse('outreach:clinicdetail',args=[self.id])
