from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime

from .permissions import IsOwnerStoreFrontOrReadOnly, IsOwnerServiceOrReadOnly
from .serializer import ServiceSerializer, StoreFrontSerializer, ListaServicesPorStoreFrontSerializer, UserAccountSerializer, BookingSerializer
from .models import Booking, UserAccount, StoreFront, Services


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
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerStoreFrontOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ListaServicesPorStoreFront(generics.ListAPIView):
    """"Listando todos os Services de um dado StoreFront"""

    def get_queryset(self):
        queryset = Services.objects.filter(store_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaServicesPorStoreFrontSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    """Listando e criando os Services cadastrados"""
    model = Services
    serializer_class = ServiceSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerServiceOrReadOnly]

    def get_queryset(self):
        queryset = Services.objects.filter(
            store=self.kwargs['storefront_id'])
        return queryset

    def perform_create(self, serializer):
        """Cria um novo service e associa ao StoreFront"""
        serializer.save(store_id=self.kwargs['storefront_id'])

    def retrieve(self, request, pk=None, storefront_id=None):
        """Retorna um service específico"""
        queryset = Services.objects.filter(
            store_id=storefront_id)
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def update(self, request, pk=None, storefront_id=None):
        """Atualiza um service específico"""
        queryset = Services.objects.filter(
            store_id=self.kwargs['storefront_id'])
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, storefront_id=None):
        """Realiza a atualização parcial de um service específico"""
        queryset = Services.objects.filter(
            store_id=self.kwargs['storefront_id'])
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(
            service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingViewSet(viewsets.ModelViewSet):
    """Listando as Bookings cadastradas"""
    serializer_class = BookingSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.filter(
            user=self.request.user, service=self.kwargs['service_id'])
        return queryset
