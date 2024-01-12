from django.contrib import admin
from .models import Bookclinic, Booktheatre


# Register your models here.
class BookclinicAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','clinic','phone','tcadate','doctornote','date']
admin.site.register(Bookclinic, BookclinicAdmin)

class BooktheatreAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','typeofoperation','phone','dateofoperation','doctor','date']
admin.site.register(Booktheatre, BooktheatreAdmin)