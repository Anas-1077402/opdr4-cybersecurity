from typing import Any
from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm
from .models import User
from main.models import Beperkingen, Toezichthouders


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
        self.fields['geboortedatum'].widget.attrs.update({'class': 'form-control', 'type': "date", 'id': "geboortedatum", 'onchange': "ageChecker()"})
        self.fields['gebruikte_hulpmiddelen'].widget.attrs.update({'class': 'form-control'})
        self.fields['bijzonderheden'].widget.attrs.update({'class': 'form-control'})
        self.fields['bijzonderheden_beschikbaarheid'].widget.attrs.update({'class': 'form-control'})


class BeperkingForm(forms.Form):
    beperkingen = forms.ModelMultipleChoiceField(queryset=Beperkingen.objects.all(), widget=forms.CheckboxSelectMultiple)


class ToezichthoudersForm(forms.ModelForm):
    voornaam_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    achternaam_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefoonnummer_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    voornaam_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    achternaam_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    telefoonnummer_2 = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    ervaringsdeskundige = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Toezichthouders
        fields = (
            'voornaam_1', 'achternaam_1', 'telefoonnummer_1',
            'voornaam_2', 'achternaam_2', 'telefoonnummer_2', 'ervaringsdeskundige'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['voornaam_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['achternaam_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefoonnummer_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['voornaam_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['achternaam_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefoonnummer_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['ervaringsdeskundige'].widget.attrs.update({'class': 'form-control'})