from django.shortcuts import render,redirect

# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

from testapp.models import Appointment
def insert_appointment(request):
    if request.method=='POST':
        pn = request.POST.get("pn")
        doc = request.POST.get("doc")
        date = request.POST.get("date")
        time = request.POST.get("time")
        appt = Appointment(pn=pn, doc=doc, date=date, time=time)
        appt.save()
        return redirect('thanks')
    return render(request,'testapp/appointment.html')


def service_view(request):
    return render(request,'testapp/services.html')

def doctor_view(request):
    return render(request,'testapp/doctors.html')

def about_view(request):
    return render(request,'testapp/aboutus.html')

def thanks_view(request):
    return render(request,'testapp/thank.html')

def contact_view(request):
    return render(request,'testapp/contact.html')