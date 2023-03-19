from rest_framework import serializers
from .models import Booking, StoreFront, Services, UserAccount


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
        fields = ['id',
                  'creator',
                  'creator_id',
                  'background',
                  'name',
                  'logo',
                  'theme',
                  'description',
                  'is_schedulable',
                  'address_text',
                  'address_CEP',
                  'phone',
                  'opening_time',
                  'closing_time',
                  'facebook',
                  'instagram',
                  'youtube']


class ServiceSerializer(serializers.ModelSerializer):
    store = serializers.ReadOnlyField(source='store.id')

    class Meta:
        model = Services
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        service = data['service']
        duration = service.duration
        start_time = data['start_time']
        end_time = start_time + duration
        store = service.store
        bookings = Booking.objects.filter(service__store=store)
        for booking in bookings:
            if booking.start_time <= start_time <= booking.end_time or booking.start_time <= end_time <= booking.end_time:
                raise serializers.ValidationError(
                    "The service has no available time")
        return data
