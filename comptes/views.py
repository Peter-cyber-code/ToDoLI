from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide username and password'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username, password=password).exists():
       return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST) 

    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home-user')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login_user.html', {'form': form})

@api_view(['POST'])
def login_user_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


"""def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None: # ou if user:
            login(request, user)
            return redirect('home-user')
        else:
            messages.error(request, "Nom ou mot de passe est incorrecte.")
    return render(request, 'login_user.html')"""

def logout_user(request):
    logout(request)
    return redirect('home')

