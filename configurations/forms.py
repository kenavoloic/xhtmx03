# configurations/forms.py
from django import forms
from .models import Conducteur

class ConducteurForm(forms.ModelForm):
    class Meta:
        model = Conducteur
        fields = ['nom', 'prenom', 'date_naissance', 'date_embauche']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'date_naissance': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'date_embauche': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'date_naissance': 'Date de naissance',
            'date_embauche': 'Date d\'embauche',
        }
