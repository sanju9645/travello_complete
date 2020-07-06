from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
   
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    #path('index/',TemplateView.as_view(template_name="index.html")),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),
    path('destinations/',TemplateView.as_view(template_name="destinations.html")),
    path('elements/',TemplateView.as_view(template_name="elements.html")),
    path('news/',TemplateView.as_view(template_name="news.html")), 
  
    

   
]