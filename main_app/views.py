from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Talent, Learn, Quest, Accept
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Now


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def maps_index(request):
    return render(request, 'maps/index.html')

@login_required
def talents_index(request):
    talents = Talent.objects.filter(user=request.user)
    learns = Learn.objects.filter(user=request.user)
    count= Talent.objects.filter(user=request.user).count()
    return render(request, 'talents/index.html', { 'talents': talents, 'learns': learns, 'count': count })
    

@login_required
def quests_index(request):
    quests = Quest.objects.filter(user=request.user)
    accepts = Accept.objects.filter(user=request.user)
    count= Quest.objects.filter(user=request.user).count() 
    return render(request, 'quests/index.html', { 'quests': quests, 'accepts': accepts, 'count': count })


# Talent
class TalentCreate(LoginRequiredMixin,CreateView):
  model = Talent
  fields = ['skill', 'setting', 'leveling', 'image', 'color']
  
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class TalentUpdate(LoginRequiredMixin, UpdateView):
  model = Talent
  fields = ['skill', 'setting', 'leveling', 'image', 'color']

class TalentDelete(LoginRequiredMixin, DeleteView):
  model = Talent
  success_url = '/talents/'


# Learn
class LearnCreate(LoginRequiredMixin, CreateView):
  model = Learn
  fields = ['skill']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class LearnUpdate(LoginRequiredMixin, UpdateView):
  model = Learn
  fields = ['skill']

class LearnDelete(LoginRequiredMixin, DeleteView):
  model = Learn
  success_url = '/talents/'


# Quest
class QuestCreate(LoginRequiredMixin, CreateView):
  model = Quest
  fields = ['name', 'description', 'status', 'image', 'color']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class QuestUpdate(LoginRequiredMixin, UpdateView):
  model = Quest
  fields = ['name', 'description', 'status', 'image', 'color']

class QuestDelete(LoginRequiredMixin, DeleteView):
  model = Quest
  success_url = '/quests/'


# Accept
class AcceptCreate(LoginRequiredMixin, CreateView):
  model = Accept
  fields = ['name', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class AcceptUpdate(LoginRequiredMixin, UpdateView):
  model = Accept
  fields = ['name', 'description']

class AcceptDelete(LoginRequiredMixin, DeleteView):
  model = Accept
  success_url = '/quests/'

# Signup
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)