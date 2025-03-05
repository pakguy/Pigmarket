# forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .models import Breeds as Breed
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        help_text='Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.',
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name']

class TagsColourForm(forms.ModelForm):
    class Meta:
        model = TagsColour
        fields = ['name']

class SexForm(forms.ModelForm):
    class Meta:
        model = Sex
        fields = ['name']
