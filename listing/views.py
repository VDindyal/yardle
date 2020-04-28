from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import permission_required, login_required
from home.models import Profile
from django.shortcuts import redirect

def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def construction(request):
    template = loader.get_template("listing/construction.html")
    x = list(Profile.objects.all().filter(corp_type='Construction').values())
    context = {}
    context['profiles'] = x
    return HttpResponse(template.render(context, request))

@login_required
@permission_required('listing.add_listing', raise_exception=True)
def financing(request):
    template = loader.get_template("listing/financing.html")
    x = list(Profile.objects.all().filter(corp_type='Financing').values())
    context = {}
    context['profiles'] = x
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
    if request.method == 'GET':
        template = loader.get_template("listing/property.html")
        x = list(Profile.objects.all().filter(corp_type='Property Management').values())
        context = {}
        context['profiles'] = x
        return HttpResponse(template.render(context, request))
    else:
        return redirect('home:home')
