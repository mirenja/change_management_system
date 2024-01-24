"""" Defines urls for learning logs"""
from django.urls import path

#path fucntion maps urls to views
from . import views
app_name = 'learninglog'

urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    #url for all topics
    path('topics/',views.topics,name='topics'),
    #url for individual topics
    path('topics/<int:topic_id>/', views.topic,name='topic')
]