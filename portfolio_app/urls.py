from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project, name='project'),

    #crud
    path('add-project/', views.addProject, name='addProject'),
    path('update-project/<slug:slug>/', views.updateProject, name='updateProject'),
    path('delete-project/<slug:slug>/', views.deleteProject, name='deleteProject'),

	path('send_email/', views.sendEmail, name="send_email"),
]