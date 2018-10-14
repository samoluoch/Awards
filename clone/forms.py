from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project,ContentRating,UsabilityRating,DesignRating

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date', 'profile', 'rating']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = ['rating', 'comment']


class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating', 'comment']


class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignRating
        fields = ['rating', 'comment']

