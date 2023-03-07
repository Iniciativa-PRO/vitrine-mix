from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from vitrine.models import UserAccount
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
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message': 'User logged out'}, safe=False)
    else:
        return JsonResponse({'error': 'User is not logged in'}, safe=False)


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.POST.get('profile_picture')
        try:
            user = UserAccount.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name, profile_picture=profile_picture)
            if user is not None:
                login(request, user)
                return JsonResponse({'user': user.username}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)
    else:
        return JsonResponse({'error': 'Wrong method'}, safe=False)


@csrf_exempt
def get_user(request):
    if request.user.is_authenticated:
        return JsonResponse({'username': request.user.username, 'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'profile_picture': request.user.profile_picture}, safe=False)
    else:
        return JsonResponse({'error': 'User is not logged in'}, safe=False)


