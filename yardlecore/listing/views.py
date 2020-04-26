from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import permission_required, login_required


def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def construction(request):
    template = loader.get_template("listing/construction.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def financing(request):
    template = loader.get_template("listing/financing.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def getstarted(request):
    template = loader.get_template("listing/getstarted.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def property(request):
    template = loader.get_template("listing/property.html")
    context = {}
    return HttpResponse(template.render(context, request))
