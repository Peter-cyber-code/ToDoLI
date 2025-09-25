from django.shortcuts import get_object_or_404, redirect, render
from taches.forms import TacheForm
from taches.models import Tache
from django.contrib.auth.decorators import login_required

from taches.serializers import TacheSerializer

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def home_user(request):
    taches = Tache.objects.filter(utilisateur=request.user)
    return render(request, 'home_user.html', {'taches': taches})

@login_required
def ajouter_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.utilisateur = request.user
            tache.save()
            return redirect('liste-taches')
    else:
        form = TacheForm()
    return render(request, 'ajouter_tache.html', {'form': form})

@login_required
def liste_taches(request):
    taches = Tache.objects.filter(utilisateur=request.user)
    return render(request, 'liste_taches.html', {'taches': taches})

@login_required
def modifier_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, utilisateur=request.user)
    if request.method == 'POST':
        tache.titre = request.POST['titre']
        tache.description = request.POST['description']
        tache.complet = 'complet' in request.POST
        tache.save()
        return redirect('home-user')
    return render(request, 'modifier_tache.html', {'tache': tache})

@login_required
def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, utilisateur=request.user)
    if request.method == 'POST':
        tache.delete()
        return redirect('home-user')
    return render(request, 'supprimer_tache.html', {'tache': tache})


"""On va juste creer les api ici"""

from rest_framework import generics, permissions

#Vue pour lister et creer des taches via l'API
class TacheListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tache.objects.all() # On commence avec toutes les taches
    serializer_class = TacheSerializer # le serializer à utiliser
    permission_classes = [permissions.IsAuthenticated] # l'utilisateur doit etre connecte

    def get_queryset(self):
        return Tache.objects.filter(utilisateur=self.request.user)

    #Lors de la creation, on associe la tache à l'utilisateur connecté
    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)

#Vue pour Voir, modifier ou supprimer une tache spécifique
class TacheRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer
    permission_classes = [permissions.IsAuthenticated]

    #On restreint l'accès: un utilisateur ne peut voir que ses propres
    def get_queryset(self):
        return Tache.objects.filter(utilisateur=self.request.user)
    

from rest_framework.views import APIView
from rest_framework.response import Response
class UserProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response ({
            'id': user.id,
            'username': user.username,
        })







