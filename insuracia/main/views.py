from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


# Create your views here.
class MainListView(ListView):
    # template_name = 'main/index.html'
    model = Article
