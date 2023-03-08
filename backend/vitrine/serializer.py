from rest_framework import serializers
from .models import StoreFront, Services


class ListaServicesPorStoreFrontSerializer(serializers.ModelSerializer):
    store_id = serializers.ReadOnlyField(source='store.id')

    class Meta:
        model = Services
        fields = '__all__'


class StoreFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreFront
        fields = '__all__'
