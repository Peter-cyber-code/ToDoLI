from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tache(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    titre = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    complet = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.titre 
    
    