from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template("listing/create.html")
    context = {}
    return HttpResponse(template.render(context, request))
