from django import forms
from momo.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    picture = forms.ImageField(required = False)
    class Meta():
        model = UserProfile
        fields = ('picture',)
