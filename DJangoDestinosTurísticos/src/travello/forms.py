from django import forms
from django.forms import ModelForm
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
            'name',
            'img',
            'desc',
            'price',
            'offer',
        ]

class RawDestinationForm(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()
    desc = forms.CharField(
        widget= forms.Textarea()
    )
    price = forms.IntegerField()
    offer = forms.BooleanField()
