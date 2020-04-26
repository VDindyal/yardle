from django.urls import path

from . import views

app_name = 'listing'
urlpatterns = [
    path('', views.index, name='index'),
    path('construction', views.construction, name='construction'),
    path('financing', views.financing, name='financing'),
    path('getstarted', views.getstarted, name='getstarted'),
    path('property', views.property, name='property'),
]
