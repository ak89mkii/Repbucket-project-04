from django.shortcuts import render
# from .models import Skill,


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def skills_index(request):
#   skills = Skill.objects.filter(user=request.user)
#   return render(request, 'skills/index.html', { 'skills': skills })