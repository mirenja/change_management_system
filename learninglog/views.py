from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """homepage for the app"""
    return render(request, 'learninglog/index.html')


def topics(request):
    """"shows all the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learninglog/topics.html', context)

def topic(request,topic_id):
    """shows single topic"""
    topic= Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learninglog/topic.html',context)
