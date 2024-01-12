from django.contrib import admin
from .models import Post, Homepage, Aboutpage, Newsletter, Post, Apointment
from .models import Contact ,Post #,New
from .models import New
# Register your models here.

#admin.site.register(Post)
admin.site.register(Homepage)
admin.site.register(Aboutpage)
admin.site.register(Newsletter)
#admin.site.register(New)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content']
admin.site.register(Contact, ContactAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['first_name','second_name','patient_category','phone_number','file_number','age','id_number','file_identity']
admin.site.register(Post, PostAdmin)


admin.site.register(Apointment)



class NewAdmin(admin.ModelAdmin):
    list_display = ['first_name','second_name','phone_number','age','id_number','file_no']