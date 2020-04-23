from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('how', views.how, name="how"),
    path('logout', views.user_logout, name='user_logout')
]
