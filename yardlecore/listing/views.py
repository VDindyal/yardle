from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def construction(request):
    template = loader.get_template("listing/construction.html")
    context = {}
    return HttpResponse(template.render(context, request))

def financing(request):
    template = loader.get_template("listing/financing.html")
    context = {}
    return HttpResponse(template.render(context, request))

def getstarted(request):
    template = loader.get_template("listing/getstarted.html")
    context = {}
    return HttpResponse(template.render(context, request))

def property(request):
    template = loader.get_template("listing/property.html")
    context = {}
    return HttpResponse(template.render(context, request))
