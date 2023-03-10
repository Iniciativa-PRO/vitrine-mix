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
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    background = serializers.ImageField(required=False)
    logo = serializers.ImageField(required=False)

    class Meta:
        model = StoreFront
        fields = ['id', \
                  'creator', \
                  'creator_id', \
                  'background', \
                  'name', \
                  'logo', \
                  'theme', \
                  'description',\
                  'is_schedulable', \
                  'address_text', \
                  'address_CEP', \
                  'phone', \
                  'opening_time', \
                  'closing_time', \
                  'facebook', \
                  'instagram', \
                  'youtube']
