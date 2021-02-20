from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import extendeduser
from django.contrib.auth.models import User

class CustomUsercreationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	first_name=forms.CharField(max_length=30)
	last_name=forms.CharField(max_length=30)
	class Meta:
		model=User
		fields=('username','email','first_name','last_name','password1','password2')




class extendeduserForm(forms.ModelForm):
	class Meta:
		model=extendeduser
		fields=('Contact_no','Service_No','Address','Rank','Trade','Section','Unit','Ip_NO')

		