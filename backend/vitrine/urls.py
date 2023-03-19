from django.urls import path, include
from rest_framework import routers


from . import views
from .views import ListaServicesPorStoreFront, ServiceViewSet, StoreFrontViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register('storefronts', StoreFrontViewSet, basename='StoreFront')
router.register('useraccounts', views.UserAccountViewSet,
                basename='UserAccount')

services_detail = ServiceViewSet.as_view({
    'get': 'retrieve',
})
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('profile', views.get_user),
    path('', include(router.urls)),
    path('storefront/<int:pk>/services', ListaServicesPorStoreFront.as_view()),
    path('storefronts/<int:storefront_id>/services/', ServiceViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('storefronts/<int:storefront_id>/services/<int:pk>', ServiceViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('storefront/<int:store>/services/<int:service_id>/bookings',
         BookingViewSet.as_view())

]
