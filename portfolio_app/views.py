from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .decorators import *

from .models import *
from .forms import *

# Create your views here.

app_name = 'portfolio_app'
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'portfolio_app/index.html', context)

def project(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'portfolio_app/project.html', context)

#crud
@admin_only
@login_required(login_url="home")
def addProject(request):
	form = addProjectForm()

	if request.method == 'POST':
		form = addProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('home')

	context = {'form':form}
	return render(request, 'portfolio_app/add_project.html', context)

@admin_only
@login_required(login_url="home")
def updateProject(request, slug):
    post = Post.objects.get(slug=slug)
    form = addProjectForm(instance=post)

    if request.method == 'POST':
        form = addProjectForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'portfolio_app/add_project.html', context)

@admin_only
@login_required(login_url="home")
def deleteProject(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'item':post}
    return render(request, 'portfolio_app/delete_project.html', context)

def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('portfolio_app/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['portfolio.triefauzan@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'portfolio_app/email_sent.html')
