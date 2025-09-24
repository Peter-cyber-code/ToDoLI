from django import forms
from taches.models import Tache 


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache 
        exclude = ['utilisateur'] # ne pas afficher l'utilisateur

        