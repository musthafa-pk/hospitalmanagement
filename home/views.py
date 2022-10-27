from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
from .models import Doctors

from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return  render(request,'about.html')
def booking(request):
    if request.method  == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conform.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return  render(request,'booking.html', dict_form)
def doctors(request):
    dic_doc ={
            'doctors':Doctors.objects.all(),
    }
    return  render(request,'doctors.html',dic_doc)
def contact(request):
    return  render(request,'contact.html')
def department(request):
    dict_dept = {
        'dept':Departments.objects.all(),
    }
    return render(request,'department.html',dict_dept)