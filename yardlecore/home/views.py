from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Profile
from django import forms

class CorporateSignupForm(UserCreationForm):
    corp_name = forms.CharField(required=True, label="Corporation Name", max_length=128)
    years_incorporated = forms.IntegerField(required=True, min_value=0, label="Years Incorporated")
    corp_type = forms.ChoiceField(choices = Profile.CORP_TYPES, required=True, label="Corporation Type", widget=forms.Select(attrs={'class':'form-control'}))
    service_cost = forms.FloatField(required=True, label="Service Cost")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'corp_name', 'years_incorporated', 'corp_type', 'service_cost')

# Create your views here.
def home(request):
    template = loader.get_template("home/home.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='StandardUser')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user_auth = authenticate(username=username, password=raw_password)
            login(request, user_auth)
            return redirect('home:home')  # user profile page maybe?
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def signup_corporate(request):
    if request.method == 'POST':
        form = CorporateSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.corp_name = form.cleaned_data.get('corp_name')
            user.profile.years_incorporated = form.cleaned_data.get('years_incorporated')
            user.profile.corp_type = form.cleaned_data.get('corp_type')
            user.profile.service_cost = form.cleaned_data.get('service_cost')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home:home')
    else:
        form = CorporateSignupForm()
    return render(request, 'home/signup_corporate.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'home:home'))
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'home/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'home/signin.html', {'form': form})

def how(request):
    template = loader.get_template("home/how.html")
    context = {}
    return HttpResponse(template.render(context, request))

def user_logout(request):
    logout(request)
    return redirect('home:home')
