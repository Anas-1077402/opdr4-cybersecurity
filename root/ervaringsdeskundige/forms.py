from typing import Any
from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm
from .models import User
from main.models import Beperkingen


class RegisterForm(UserCreationForm):
    geboortedatum = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'postcode', 'geslacht','email', 'telefoonnummer', 'geboortedatum', 'gebruikte_hulpmiddelen',
                  'bijzonderheden', 'bijzonderheden_beschikbaarheid', 'username',)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['postcode'].widget.attrs.update({'class': 'form-control'})
        self.fields['geslacht'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefoonnummer'].widget.attrs.update({'class': 'form-control'})
        self.fields['geboortedatum'].widget.attrs.update({'class': 'form-control'})
        self.fields['gebruikte_hulpmiddelen'].widget.attrs.update({'class': 'form-control'})
        self.fields['bijzonderheden'].widget.attrs.update({'class': 'form-control'})
        self.fields['bijzonderheden_beschikbaarheid'].widget.attrs.update({'class': 'form-control'})



class BeperkingForm(forms.Form):
    beperkingen = forms.ModelMultipleChoiceField(queryset=Beperkingen.objects.all(), widget=forms.CheckboxSelectMultiple)
