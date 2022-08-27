from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm

class UserModelForm(UserCreationForm):
	class Meta:
		model = User
		fields = '__all__'

class UserUpdateModelForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'profile_pic']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name'})
		self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name'})

class CustomLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(CustomLoginForm, self).__init__(*args, **kwargs)
		self.fields['login'].widget.attrs.update({
			'placeholder': 'Username or Email',
			'class': 'textinput form-control'
		})
		self.fields['login'].label = 'Username or Email'
		self.fields['remember'].widget.attrs.update({
			'checked': 'true'
		})