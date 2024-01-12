
from django.db import models
from django.contrib.auth.models import User
#from utils import create_new_ref_number
from uuid import uuid4


class Newid(models.Model):
    first_name = models.CharField(max_length=15)
    id_number = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    patientid = models.FileField(upload_to='images/%Y/%m/%d', blank=False)
    
    def __str__(self):
        return self.first_name


    class Meta:
        ordering = ('-created_at', )
    #    verbose_name = 'category'
    #    verbose_name_plural = 'categories'