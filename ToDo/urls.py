
from django.contrib import admin
from django.urls import path
from comptes.views import login_user, login_user_api, logout_user, register_user, signup
from taches.views import TacheListCreateAPIView, TacheRetrieveUpdateDestroyAPIView, UserProfileAPIView, ajouter_tache, home, home_user, liste_taches, modifier_tache, supprimer_tache
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home-user', home_user, name='home-user'),
    path('ajouter-tache', ajouter_tache, name='ajouter-tache'),
    path('liste-taches', liste_taches, name='liste-taches'),
    path('login-user', login_user, name='login-user'),
    path('signup', signup, name='signup'),
    path('logout-user', logout_user, name='logout-user'),
    path('supprimer-tache/<int:tache_id>/', supprimer_tache, name='supprimer-tache'),
    path('modifier-tache/<int:tache_id>/', modifier_tache, name='modifier-tache'),
    path('api/taches/', TacheListCreateAPIView.as_view(), name='api-taches'),
    path('api/taches/<int:pk>/', TacheRetrieveUpdateDestroyAPIView.as_view(), name='update-tache'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api/register/', register_user, name='register'),
    path('api/login/', login_user_api, name='connexion'),
    path('api/user/', UserProfileAPIView.as_view(), name='user-profile'),
]

