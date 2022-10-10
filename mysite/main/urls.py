
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index,name='index'),
     path('<int:Category_id>/mains/',views.getCategory,name='post'),
   
] 