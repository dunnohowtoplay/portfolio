from django import forms
from django.forms import ModelForm

from .models import Post

class addProjectForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}