from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

app_name = 'portfolio_app'
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'portfolio_app/index.html', context)