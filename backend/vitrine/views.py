from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
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


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Login request


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successful")
        else:
            return HttpResponse("Login failed")
    else:
        return HttpResponse("Wrong method")

    # return HttpResponse(f'USer:{username} password: {password}, user: {user}')


@csrf_exempt
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("Logout successful")
    else:
        return HttpResponse("user was not logged in")


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
                return HttpResponse("Register successful")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Wrong method")


@csrf_exempt
def get_user(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user)
    else:
        return HttpResponse("User is not logged in")
