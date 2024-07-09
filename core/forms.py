from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContratoCreation(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'
        labels = {
            'appaterno': 'Apellido Paterno',
            'apmaterno': 'Apellido Materno',
        }
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'class': 'datepicker'}),
            'fecha_termino': forms.TextInput(attrs={'class': 'datepicker'}),
        }

class RepCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este usuario ya existe!")
        return username