from django.shortcuts import render,redirect
from hospitalapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def departments(request):
    return render(request, 'departments.html')
def doctors(request):
    return render(request, 'doctors.html')
def appoint(request):
    if request.method == "POST":
       myappointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
       myappointment.save()
       return redirect('/appointment')
    else:
        return render(request,'appointment.html')





def contact(request):
    if request.method == "POST":
       contact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
       contact.save()
       return redirect('/contact')
    else:
        return render(request,'contact.html')

