from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )
    
    phone_number = forms.CharField(
        max_length=15,
        label='Номер телефона',
        widget=forms.NumberInput(attrs={'class': 'form-input'}),
    )
    
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    
    password2 = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )
        
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'birth_date', 'bio', )