from django.db.models.signals import post_save  # signal appelé après sauvegarde
from django.dispatch import receiver # Permet d'enregistrer une fonction comme écouteur
from django.contrib.auth.models import User #Modele utilisateur Django
from rest_framework.authtoken.models import Token


# cette fonction sera éxecutée chaque fois qu'un utilisateur est créé
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:  # si c'est un nouvel utilisateur
        Token.objects.create(user=instance) # crée un token pour cet utilisateur
        