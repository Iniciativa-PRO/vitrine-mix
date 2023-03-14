from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ListaServicesPorStoreFront, StoreFrontViewSet

router = routers.DefaultRouter()
router.register('storefronts', StoreFrontViewSet, basename='StoreFront')
router.register('useraccounts', views.UserAccountViewSet,
                basename='UserAccount')

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('profile', views.get_user),
    path('', include(router.urls)),
    path('storefront/<int:pk>/services', ListaServicesPorStoreFront.as_view())

]
