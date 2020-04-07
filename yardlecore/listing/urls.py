from django.urls import path

from . import views

app_name = 'listing'
urlpatterns = [
    path('create', views.create, name='create'),
    path('', views.index, name='index')
]
