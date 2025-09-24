from rest_framework import serializers
from .models import Tache 

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache 
        fields = ['id', 'titre', 'description', 'complet', 'utilisateur']
        