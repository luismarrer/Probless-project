from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Owner

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is obligatory.')
        return email