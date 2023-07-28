from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import Upload

from django import forms
# from captcha.fields import CaptchaField


class CreateUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['PetName','YourName','ShortDescription','Instructions','Photo']


class UserForm(forms.Form):
    username = forms.CharField(label="userName", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="passWord", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': "Password"}))
    # captcha = CaptchaField(label='captcha')

class RegisterForm(forms.Form):
    gender = (
        ('male', "male"),
        ('female', "female"),
    )
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Gender', choices=gender)
    # captcha = CaptchaField(label='Captcha')

