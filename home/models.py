
from django.db import models
from django.contrib.auth.models import User
#from utils import create_new_ref_number
from uuid import uuid4
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
def generateUUID():
    return str(uuid4())



class PostManager(models.Manager):
 
    def get_queryset(self):
        return super(PostManager, self).get_queryset()\
            .filter(status='first_name')



class Post(models.Model):
    first_name = models.CharField(max_length=500)
    second_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15, blank=True)
    file_number = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(max_length=3,blank=True)
    id_number = models.CharField(max_length=50, blank=True)
    patient_category = models.CharField(max_length=500, blank=True,choices=(
                                            ('InPatient','InPatient'),
                                            ('OutPatient','OutPatient'),
                                            ('Maternity','Maternity'),
                                            ('Special_Clinic','Special_Clinic')))
    #slug = models.SlugField(max_length=150, unique=True, db_index=True)
    file_identity = models.CharField(default=generateUUID, max_length=6, unique=True, editable=False)
    tags = TaggableManager
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False) 
    
  
    def __str__(self):
        return self.first_name

    def get_absolute_re_path(self):
        return reverse('home:postdetail', args=[self.id])
    
    class Meta:
        ordering = ('-created_at', )
    #    verbose_name = 'category'
    #    verbose_name_plural = 'categories'

class AssociatedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='associated_posts')
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


class PostManager(models.Manager):
 
    def get_queryset(self):
        return super(PostManager, self).get_queryset()\
            .filter(status='first_name')






class New(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    phone_number = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    id_number = models.IntegerField(blank=True)
    patient_category = models.CharField(max_length=500, blank=True,choices=(
                                            ('InPatient','InPatient'),
                                            ('OutPatient','OutPatient'),
                                            ('Maternity','Maternity'),
                                            ('Special_Clinic','Special_Clinic')))
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    file_no = models.AutoField(primary_key=True)

    def __str__(self):
        return self.first_name

    #class Meta:
     #   ordering = ('-created_at')




class Note(models.Model):
    #user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Homepage(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=700,blank=True)
    image = models.URLField(max_length=350, blank=True)

    title1 = models.CharField(max_length=500)
    content1 = models.CharField(max_length=700, blank=True)
    image1 = models.URLField(max_length=350, blank=True)
 
    def __str__(self):
        return self.title

class Aboutpage(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image =models.URLField(max_length=350, blank=True)
    image1 = models.URLField(max_length=350, blank=True)

    aboutus = models.TextField(max_length=500, blank=True)
    aboutimage = models.URLField(max_length=350, blank=True)

    story = models.TextField(max_length=1500, blank=True)
    storyimage = models.URLField(max_length=350, blank=True)

    team = models.TextField(max_length=1500, blank=True)
    teamimage = models.URLField(max_length=350, blank=True)
    whyus = models.TextField(max_length=1500, blank=True)
    whyusimage = models.URLField(max_length=350, blank=True)

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email



class Apointment(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    request = models.TextField(blank=True)
    file_number = models.IntegerField(blank=True,default=False)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-accepted_date"]
