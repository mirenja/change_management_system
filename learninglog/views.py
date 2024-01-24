from django.shortcuts import render

# Create your views here.

def index(request):
    """homepage for the app"""
    return render(request, 'learninglog/index.html')
