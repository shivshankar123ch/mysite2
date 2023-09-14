from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Personal_Information)
admin.site.register(Job_Information)
admin.site.register(Employee_Education_Information)
admin.site.register(Employee_Old_Service_History)
admin.site.register(Declaration)
