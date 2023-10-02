# accounts/forms.py

from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class BootstrapStyleFormMixin:
    def __init__(self, *args, **kwargs):
        super(BootstrapStyleFormMixin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CustomUserCreationForm(BootstrapStyleFormMixin, UserCreationForm):
    pass

class CustomAuthenticationForm(BootstrapStyleFormMixin, AuthenticationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'date_of_birth', 'address', 'bio', 'profile_picture']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date', 'placeholder': 'Date of Birth'}),
            'address': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 3, 'placeholder': 'Address'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 5, 'placeholder': 'Bio'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-2'}),
        }
