from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def contact(request):
    template = loader.get_template("home/contact.html")
    context = {}
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template("home/home.html")
    context = {}
    return HttpResponse(template.render(context, request))
