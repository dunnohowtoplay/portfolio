from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name = 'portfolio_app'
def home(request):
    return render(request, 'portfolio_app/index.html')