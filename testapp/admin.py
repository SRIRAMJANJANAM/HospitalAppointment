from django.contrib import admin
from testapp.models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','pn','doc','date','time']
admin.site.register(Appointment,AppointmentAdmin)
