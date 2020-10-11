from django.shortcuts import render, redirect
from .models import Talent


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def talents_index(request):
    talents = Talent.objects.all()
#   talents = Talent.objects.filter(user=request.user)
    return render(request, 'talents/index.html', { 'talents': talents })