from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import translation
from .models import News
from django.shortcuts import render

def home(request):
    articles = News.objects.all()
    return render(request, "home.html", {"articles": articles})

