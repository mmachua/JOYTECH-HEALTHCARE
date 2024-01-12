
from django.db import models
from django.conf import settings
#from django.contrib.auth import timezone

class Post(models.Model):
    
    post = models.CharField(max_length=500 ,blank=False)
    
    document = models.FileField(null = True,  blank=False, upload_to='documents/%Y/%m/%d')
   
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.post

    class Meta:
        ordering = ('-date', )
    #    verbose_name = 'category'
    #    verbose_name_plural = 'categories'

 