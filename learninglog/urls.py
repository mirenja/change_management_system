"""" Defines urls for learning logs"""
from django.urls import path

#path fucntion maps urls to views
from . import views
app_name = 'learninglog'

urlpatterns = [
    #Home page
    path('',views.index,name='index')
]