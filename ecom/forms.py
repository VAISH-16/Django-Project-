from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cart.models import Contact

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ContactForm(forms.ModelForm):  # Inherit from forms.ModelForm
    class Meta:
        model = Contact
        fields = '__all__'
