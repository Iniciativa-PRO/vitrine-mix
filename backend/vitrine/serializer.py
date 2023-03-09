from rest_framework import serializers
from .models import StoreFront, Services, UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'profile_picture']


class ListaServicesPorStoreFrontSerializer(serializers.ModelSerializer):
    store_id = serializers.ReadOnlyField(source='store.id')

    class Meta:
        model = Services
        fields = '__all__'


class StoreFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreFront
        fields = '__all__'
