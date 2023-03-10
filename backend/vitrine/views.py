from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from .serializer import StoreFrontSerializer, ListaServicesPorStoreFrontSerializer, UserAccountSerializer
from .models import UserAccount, StoreFront, Services


# Create your views here.


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return


# Login request


@csrf_exempt
def login_view(request):
    """Loga o usuário"""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'User logged in'}, safe=False)
        else:
            return JsonResponse({'error': 'User not found'}, safe=False)
    else:
        return JsonResponse({'error': 'Wrong method'}, safe=False)


@csrf_exempt
def logout_view(request):
    """Desloga o usuário"""
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'User logged out'}, safe=False)
    else:
        return JsonResponse({'error': 'User is not logged in'}, safe=False)


@csrf_exempt
def register(request):
    """Cadastra um novo usuário"""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES['profile_picture']
        try:
            user = UserAccount.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                profile_picture=profile_picture)
            if user is not None:
                login(request, user)
                return JsonResponse({'user': user.username}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Wrong method'}, safe=False)


@csrf_exempt
def get_user(request):
    """Retorna os dados do usuário logado"""
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 'email': request.user.email, 'first_name': request.user.first_name,
             'last_name': request.user.last_name, 'profile_picture': request.build_absolute_uri(request.user.profile_picture)}, safe=False)
    else:
        return JsonResponse({'error': 'User is not logged in'}, safe=False)


def delete_user(request):
    """Deleta o usuário logado"""
    if request.user.is_authenticated:
        request.user.delete()
        return JsonResponse({'message': 'User deleted'}, safe=False)
    else:
        return JsonResponse({'error': 'User is not logged in'}, safe=False)


class UserAccountViewSet(viewsets.ModelViewSet):
    """Listando os usuários cadastrados"""
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class StoreFrontViewSet(viewsets.ModelViewSet):
    """Listando as StoreFronts cadastradas"""
    queryset = StoreFront.objects.all()
    serializer_class = StoreFrontSerializer
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ListaServicesPorStoreFront(generics.ListAPIView):
    """"Listando todos os Services de um dado StoreFront"""

    def get_queryset(self):
        queryset = Services.objects.filter(store_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaServicesPorStoreFrontSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
