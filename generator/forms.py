from django.forms import ModelForm
from django import forms
from .models import QrCode


class Generator(ModelForm):
    class Meta:
        model = QrCode
        fields = ['wifi_name', 'encryption', 'password']
        widgets = {
            'password': forms.NumberInput(),
        }
