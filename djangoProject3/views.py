from django.shortcuts import render
from django.http import HttpResponse
from .forms import StatForm, StatData

from .models import Yard,Location, Running_Back, Quarter_Back


def stats(request):
    return HttpResponse("Running Back Stats")

def yards(request):
    return HttpResponse("Receiving Stats")

def qb(request):
    return HttpResponse("Quarterback Stats")

def receivers1(request):
    form = StatForm()

    return render(request, 'receivers1.html', {'form':form})

def add_data(request):
    form = StatData()

    return render(request, 'running_form.html', {'form':form})

def receivers(request):

    yards = Yard.objects.order_by('Receiver')
    runs = Running_Back.objects.order_by('Back')
    qbs =  Quarter_Back.objects.order_by('QB')
    return render(request, 'receivers.html', {'yards':yards,'runs':runs, 'qbs':qbs})

def runningbacks(request):

    runs = Running_Back.objects.order_by('Back')
    return render(request, 'runningback.html', {'runs':runs})

def qb(request):

    quarterback = Quarter_Back.objects.order_by('QB')
    return render(request, 'quarterback.html', {'quarterback': quarterback})



def return_location(request):

    locations = Location.objects.order_by('City')
    return render(request,'city.html', {'locations':locations})

def translate(request):

    return HttpResponse("You're on the translate page!" + request.GET['originaltext'])

def home(request):
    return render(request,'home.html')






