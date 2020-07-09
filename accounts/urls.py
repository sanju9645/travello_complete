from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
   
    path("register/",views.register,name='register'),
    path("login/",views.login,name='login'),
    path("logout/",views.logout,name='logout'),

    
    

   
]