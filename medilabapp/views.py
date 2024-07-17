from django.shortcuts import render, redirect
from medilabapp.models import Company, Appointment, Member


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'index.html',{'member':member})
        else:
            return render(request, 'login.html')
    else:
            return render(request, 'login.html')


def start(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'post':
        contacts = Company(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'])
        contacts.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def Patient(request):
    if request.method == 'POST':
        patient = Patient(fullname=request.POST['name'],
                          email=request.POST['email'],
                          medicalhistory=request.POST['medicalhistory'],
                          age=request.POST['age'], )

        patient.save()
        return redirect('/Patient')
    else:
        return render(request, 'patient.html')


def Appoint(request):
    if request.method == 'POST':
        appointment: Appointment = Appointment(name=request.POST['name'],
                                               email=request.POST['email'],
                                               phone=request.POST['phone'],
                                               date=request.POST['date'],
                                               department=request.POST['department'],
                                               doctor=request.POST['doctor'],
                                               message=request.POST['message'])
        appointment.save()
        return redirect('/Appointment')
    else:
        return render(request, 'appointments.html')


def show(request):
    data = Appointment.objects.all()
    return render(request, 'show.html', {'appointment': data})


def delete(request, id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')


def register(request):
    if request.method == 'POST':
        member = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
